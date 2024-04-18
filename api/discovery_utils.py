import json
import os
from ibm_watson import DiscoveryV2
from ibm_watson.discovery_v2 import TrainingExample
from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator, BearerTokenAuthenticator
from dotenv import load_dotenv
import requests
import pandas as pd
from io import StringIO

load_dotenv()

## Authentication ##
discovery_authenticator = BearerTokenAuthenticator(os.getenv('DISCOVERY_TOKEN'))
discovery_url = os.getenv('DISCOVERY_URL')
discovery_project_id = os.getenv('DISCOVERY_PROJECT_ID')

## Initialize discovery instance ##
discovery = DiscoveryV2(version='2023-12-28', authenticator=discovery_authenticator)
discovery.set_service_url(
    discovery_url
)
discovery.set_disable_ssl_verification(True)

counter=2


def get_collections():
    ## List Collections ##
    collections = discovery.list_collections(project_id=discovery_project_id).get_result()
    print("####################################### LIST COLLECTIONS")
    print(json.dumps(collections, indent=2))

    json_data = json.dumps(collections, indent=2)
    json_data = json.loads(json_data)
    collection_id = json_data["collections"][0]["collection_id"]
    return collection_id
    ## Component settings ##
    settings_result = discovery.get_component_settings(
        project_id=discovery_project_id).get_result()

    print("####################################### COMPONENTS SETTINGS")
    print(json.dumps(settings_result, indent=2))

collection_id = get_collections()


## Queries ##
#https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-query-parameters
def discovery_query(nlq:str, counter=counter):
    query_results = discovery.query(
        project_id=discovery_project_id, 
        collection_ids=[collection_id],
        #filter: str = None,
        #query=dlq,
        natural_language_query=nlq,
        #aggregation: str = None,
        return_=["metadata", "title"],
        #offset: int = None,
        #sort: str = None,
        #highlight: bool = None,
        #spelling_suggestions: bool = None,
        #table_results: 'QueryLargeTableResults' = None,
        #suggested_refinements: 'QueryLargeSuggestedRefinements' = None,
        #passages: 'QueryLargePassages' = None,
        #similar: 'QueryLargeSimilar' = None,
        count=counter).get_result()
    
    print("starting selection!")
    df = pd.DataFrame.from_dict(query_results["results"])
    df = df.fillna('')
    return df[["title", "document_passages", "metadata"]].to_dict()

#query_results_discovery = discovery_query("welche baumaßnahmen wurden im januar 2024 durchgeführt?")
#print()


#docs = discovery.list_documents(project_id=discovery_project_id, collection_id=collection_id, count=200)
#print(len(docs))

#entity_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-00000000001e')
#keyword_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-000000000018')
