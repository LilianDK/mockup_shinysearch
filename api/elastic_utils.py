import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ELASTIC_CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")

client = Elasticsearch(cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY)
print(client.info())
