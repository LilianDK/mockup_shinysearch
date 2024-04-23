from urllib.request import urlopen
import json

url = "https://raw.githubusercontent.com/elastic/elasticsearch-labs/main/datasets/workplace-documents.json"

response = urlopen(url)
data = json.load(response)

with open("data/temp.json", "w") as json_file:
   json.dump(data, json_file)


from langchain.document_loaders import JSONLoader


def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["name"] = record.get("name")
    metadata["summary"] = record.get("summary")
    metadata["url"] = record.get("url")
    metadata["category"] = record.get("category")
    metadata["updated_at"] = record.get("updated_at")

    return metadata


# For more loaders https://python.langchain.com/docs/modules/data_connection/document_loaders/
# And 3rd party loaders https://python.langchain.com/docs/modules/data_connection/document_loaders/#third-party-loaders
loader = JSONLoader(
    file_path="data/temp.json",
    jq_schema=".[]",
    content_key="content",
    metadata_func=metadata_func,
)

data[0]['url']