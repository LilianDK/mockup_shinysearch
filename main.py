from fastapi import FastAPI
from pydantic import BaseModel
from api.discovery_utils import discovery_query
app = FastAPI()

class Body(BaseModel):
    nlq: str

@app.post('/search')
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query(body.nlq)
