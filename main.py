from fastapi import FastAPI
from pydantic import BaseModel
from api.discovery_utils import discovery_query, discovery_query_2, discovery_query_3

app = FastAPI()


class Body(BaseModel):
    nlq: str
    state: str = ""

@app.post("/search")
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query(nlq=body.nlq)

@app.post("/search2")
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query_2(nlq=body.nlq, state=body.state)

@app.post("/search3")
def generate(body: Body):
    """
    Send user request to IBM discovery to find most relevant text passages.
    """
    return discovery_query_3(nlq=body.nlq, state=body.state)

# uvicorn main:app --port 8001


#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=8001)