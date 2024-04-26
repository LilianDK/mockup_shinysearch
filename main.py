from fastapi import FastAPI
from pydantic import BaseModel
from api.discovery_utils import discovery_query, discovery_query_2

app = FastAPI()


class Body(BaseModel):
    nlq: str

@app.post("/search")
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query(body.nlq)

@app.post("/search2")
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query_2(body.nlq)

# uvicorn main:app --port 8001
