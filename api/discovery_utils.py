import json
import os
from ibm_watson import DiscoveryV2
from ibm_watson.discovery_v2 import TrainingExample, QueryLargePassages
from ibm_cloud_sdk_core.authenticators import (
    CloudPakForDataAuthenticator,
    BearerTokenAuthenticator,
)
from dotenv import load_dotenv
import requests
import pandas as pd
from io import StringIO

load_dotenv()

## Authentication ##
discovery_authenticator = BearerTokenAuthenticator(os.getenv("DISCOVERY_TOKEN"))
discovery_url = os.getenv("DISCOVERY_URL")
discovery_project_id_1 = os.getenv("DISCOVERY_PROJECT_ID_1")
discovery_collection_id_1_1 = os.getenv("DISCOVERY_COLLECTION_ID_1_1")
discovery_project_id_2 = os.getenv("DISCOVERY_PROJECT_ID_2")
discovery_collection_id_2_1 = os.getenv("DISCOVERY_COLLECTION_ID_2_1")
discovery_collection_id_2_2 = os.getenv("DISCOVERY_COLLECTION_ID_2_2")
discovery_collection_id_2_3 = os.getenv("DISCOVERY_COLLECTION_ID_2_3")
discovery_collection_id_2_4 = os.getenv("DISCOVERY_COLLECTION_ID_2_4")

## Initialize discovery instance ##
discovery = DiscoveryV2(version="2023-12-28", authenticator=discovery_authenticator)
discovery.set_service_url(discovery_url)
discovery.set_disable_ssl_verification(True)

counter = 3

def get_collections():
    ## List Collections ##
    collections = discovery.list_collections(
        project_id=discovery_project_id_1
    ).get_result()
    print("####################################### LIST COLLECTIONS")
    print(json.dumps(collections, indent=2))

    json_data = json.dumps(collections, indent=2)
    json_data = json.loads(json_data)
    collection_id = json_data["collections"][0]["collection_id"]
    return collection_id
    ## Component settings ##
    settings_result = discovery.get_component_settings(
        project_id=discovery_project_id
    ).get_result()

    print("####################################### COMPONENTS SETTINGS")
    print(json.dumps(settings_result, indent=2))

collection_id = get_collections()

## Queries ##
# https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-query-parameters

# Query design for panel A front-end
def discovery_query(nlq: str, p_id=discovery_project_id_1, c_id=discovery_collection_id_1_1, counter=counter):
    query_results = discovery.query(
        project_id=p_id,
        collection_ids=[c_id],
        #filter="enriched_text.entities.text:" + state,
        #query="enriched_text.entities.text:" + state,
        natural_language_query=nlq,
        # aggregation: str = None,
        return_=["metadata", "title"],
        # offset: int = None,
        # sort: str = None,
        # highlight: bool = None,
        # spelling_suggestions: bool = None,
        # table_results: 'QueryLargeTableResults' = None,
        # suggested_refinements: 'QueryLargeSuggestedRefinements' = None,
        # similar: 'QueryLargeSimilar' = None,
        passages=QueryLargePassages(enabled=True, fields=["text"], per_document=True, max_per_document=2, characters=1000),
        count=counter,
    ).get_result()

    print("starting selection!")

    return query_results

# Query design for panel B front-end without SDU preprocessing

def discovery_query_2(nlq: str, state: str, p_id=discovery_project_id_1, c_id=[discovery_collection_id_2_1, discovery_collection_id_2_2], counter=counter):
    query_results = discovery.query(
        project_id=p_id,
        collection_ids=c_id,
        filter="enriched_text.entities.text:" + state,
        query="enriched_text.entities.text:" + state,
        natural_language_query=nlq,
        # aggregation: str = None,
        return_=["metadata", "title"],
        # offset: int = None,
        # sort: str = None,
        # highlight: bool = None,
        # spelling_suggestions: bool = None,
        # table_results: 'QueryLargeTableResults' = None,
        # suggested_refinements: 'QueryLargeSuggestedRefinements' = None,
        passages=QueryLargePassages(enabled=True, fields=["text"], per_document=True, max_per_document=2, characters=1000),
        # similar: 'QueryLargeSimilar' = None,
        count=count,
    ).get_result()

    print("starting selection!")

    return query_results

# Query design for panel B front-end with SDU preprocessing
def discovery_query_3(nlq: str, state: str, p_id=discovery_project_id_2, c_id=[discovery_collection_id_2_3, discovery_collection_id_2_4], counter=counter):
    query_results = discovery.query(
        project_id=p_id,
        collection_ids=c_id,
        filter="enriched_text.entities.text:" + state,
        query="enriched_text.entities.text:" + state,
        natural_language_query=nlq,
        # aggregation: str = None,
        return_=["metadata", "title"],
        # offset: int = None,
        # sort: str = None,
        # highlight: bool = None,
        # spelling_suggestions: bool = None,
        # table_results: 'QueryLargeTableResults' = None,
        # suggested_refinements: 'QueryLargeSuggestedRefinements' = None,
        passages=QueryLargePassages(enabled=True, fields=["text"], per_document=True, max_per_document=2, characters=1000),
        # similar: 'QueryLargeSimilar' = None,
        count=counter,
    ).get_result()
    print("starting selection!")

    return query_results

## Checking Datastructure ##
#query_results_discovery = discovery_query_2(nlq="", state="")
#query_results_discovery
#query_results_discovery = discovery_query_2(nlq="Baumaßnahmen im Januar 2024", state="Germany")
#test = query_results_discovery["matching_results"]
#test = query_results_discovery["results"]
#test

# Get a list of all documents in respective collection
#docs = discovery.list_documents(project_id=discovery_project_id_1, collection_id="98d1855e-d4f8-0154-0000-018ef0115216").get_result()

#print(docs["documents"][0])

#doclist = pd.DataFrame.from_dict(docs["documents"])

#document_id =''

#document = discovery.get_document(project_id=discovery_project_id, collection_id=collection_id, document_id=document_id).get_result()

#entity_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-00000000001e').get_result()
#keyword_list = discovery.get_enrichment(project_id=discovery_project_id, enrichment_id='701db916-fc83-57ab-0000-000000000018').get_result()
#query_results_discovery = discovery_query("Baumaßnahmen")
#test = query_results_discovery["results"][0]["document_passages"][0]["passage_text"]
#test
#df = response_data["results"][0]["document_passages"][0]["passage_text"]

## Export ##

#export = discovery.query(
#        project_id="XXXXX",
#        collection_ids=["XXXXX"],
#        filter="document_id::XXXXX",
#        # offset: int = None,
#        # count: int = None,
#).get_result()


#with open("json.json", encoding="utf8", mode="w") as json_file:
#    json.dump(export, json_file, indent=2, ensure_ascii=False)

