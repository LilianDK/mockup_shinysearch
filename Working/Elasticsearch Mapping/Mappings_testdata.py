import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/elastic/elasticsearch-labs/main/datasets/workplace-documents.json"
docs = json.loads(urlopen(url).read())

docs[0]["content"]
docs[0]["name"]
docs[0]["url"]
docs[0]["created_on"]
docs[0]["updated_at"]
docs[0]["category"]
docs[0]["rolePermissions"]