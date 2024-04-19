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

DISCOVERY_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVJaWc4MFJKMEVTeW5jVXJwZUlYZWZqUXhiMnhUSGpBUXZ4YzloTm5xWk0ifQ.eyJ1aWQiOiIxMDAwMzMxMTAwIiwidXNlcm5hbWUiOiJkb2toYWxpIiwicm9sZSI6IlVzZXIiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGVfcHJvamVjdCIsImFjY2Vzc19jYXRhbG9nIiwiY3JlYXRlX3NwYWNlIiwiY2FuX3Byb3Zpc2lvbiIsInNpZ25faW5fb25seSJdLCJncm91cHMiOlsxMDAwMSwxMDAwMF0sInN1YiI6ImRva2hhbGkiLCJpc3MiOiJLTk9YU1NPIiwiYXVkIjoiRFNYIiwiYXBpX3JlcXVlc3QiOnRydWUsImlhdCI6MTcxMzUxMjEyMX0.nEjLU7Tf2RbUlmLLq7eIJYhwaT0Fw2wakytFG8ySk30TkiOZP_eXGphCh6BT4iP5c32agLXmTkrhrSfuV3LVTDUsGABZvTawDsOI9NFP2G7Uvi0tFgz456vgyJXJyhltf8N9yNWnfnla7XSjj_gqF23mIzdGUk1JxxofAqEGSumt2ANNuFohrocui-p1PNq_P5qA57VMzeU2yxPbpqI7MiroBCdZAnYiTatn5V0C4ChchaPyUkQNBrrYQTzRgQ1xmLq4wL53mv3L-3sg8gLI9Ai33TGaXQ6EPgxrbWCh9mHQlUa_RVn-Yt185XMmqC5Vt2uR7C4G7MEyzSrehQSpJQ"
DISCOVERY_URL="https://cpd-cpd-instance.apps.aifactory-dev.dsecurecloud.de/discovery/cpd-instance-wd/instances/1703776485205351/api"
DISCOVERY_PROJECT_ID="1013ca8b-0899-4839-ac1e-984477dcf23a"

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

    return query_results

#query_results_discovery = discovery_query("welche baumaßnahmen wurden im januar 2024 durchgeführt?")
#print()


#docs = discovery.list_documents(project_id=discovery_project_id, collection_id=collection_id, count=200)
#print(len(docs))

#entity_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-00000000001e')
#keyword_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-000000000018')
