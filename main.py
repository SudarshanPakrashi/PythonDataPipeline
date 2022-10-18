from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki, wiki as wikilogic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia APIs. Call /search or /wiki"}


@app.get("/search/{name}")
async def search(name: str):
    results = search_wiki(name)
    return {"results": results}


@app.get("/wiki/{name}/{length}")
async def wiki(name: str, length: int):
    results = wikilogic(name, length)
    return {"results": results}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8086)
