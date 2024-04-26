import os
import json
import eland as ed
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from dotenv import load_dotenv
from urllib.request import urlopen

load_dotenv()

ELASTIC_CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")

client = Elasticsearch(cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY)
print(client.info())

# Setup the pipeline
CHUNK_SIZE = 400

client.ingest.put_pipeline(
    id="chunk_text_to_passages",
    processors=[
        {
            "script": {
                "description": "Chunk body_content into sentences by looking for . followed by a space",
                "lang": "painless",
                "source": """
          String[] envSplit = /((?<!M(r|s|rs)\.)(?<=\.) |(?<=\!) |(?<=\?) )/.split(ctx['text']);
          ctx['passages'] = new ArrayList();
          int i = 0;
          boolean remaining = true;
          if (envSplit.length == 0) {
            return
          } else if (envSplit.length == 1) {
            Map passage = ['text': envSplit[0]];ctx['passages'].add(passage)
          } else {
            while (remaining) {
              Map passage = ['text': envSplit[i++]];
              while (i < envSplit.length && passage.text.length() + envSplit[i].length() < params.model_limit) {passage.text = passage.text + ' ' + envSplit[i++]}
              if (i == envSplit.length) {remaining = false}
              ctx['passages'].add(passage)
            }
          }
          """,
                "params": {"model_limit": CHUNK_SIZE},
            }
        },
    ],
)


# INDEX SETUP VANILLA FROM TUTORIAL
INDEX_NAME = "chunk_passages_example"

client.indices.delete(index=INDEX_NAME, ignore_unavailable=True)

# Setup the index
client.indices.create(
    index=INDEX_NAME,
    settings={"index": {"default_pipeline": "chunk_text_to_passages"}},
    mappings={
        "dynamic": "true",
        "properties": {
            "passages": {
                "type": "nested",
                "properties": {
                    "vector": {
                        "properties": {
                            "predicted_value": {
                                "type": "dense_vector",
                                "index": True,
                                "dims": 384,
                                "similarity": "dot_product",
                            }
                        }
                    }
                },
            }
        },
    },
)

url = "https://raw.githubusercontent.com/elastic/elasticsearch-labs/main/datasets/workplace-documents.json"
docs = json.loads(urlopen(url).read())

operations = [
    {"_index": INDEX_NAME, "_id": i, "text": doc["content"], "name": doc["name"]}
    for i, doc in enumerate(docs)
]

# Add the documents to the index directly
response = helpers.bulk(
    client,
    operations,
    refresh=True,
)

def pretty_response(response):
    if len(response["hits"]["hits"]) == 0:
        print("Your search returned no results.")
    else:
        for hit in response["hits"]["hits"]:
            id = hit["_id"]
            score = hit["_score"]
            doc_title = hit["_source"]["name"]
            text = hit["_source"]["text"]
            pretty_output = f"\nID: {id}\nDoc Title: {doc_title}\nPassage Text:\n{text}"
            print(pretty_output)
            print("---")


INDEX_NAME = "chunk_passages_example"

response = client.search(
    index=INDEX_NAME, query={"match": {"text": {"query": "work"}}}
)

pretty_response(response)