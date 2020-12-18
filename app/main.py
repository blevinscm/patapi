from .routers import entries
from fastapi import Request, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles


tags_metadata = [
    {
        "name": "PAT Entries",
        "description": "API to interact with PAT API data",
        "externalDocs": {
            "description": "Administrator Landing.",
            "url": "https://aka.ms/pathack",
        },
    },
  
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="PAT API",
    description="API to interact with the Document Database in Azure Cosmos DB",
    version="v0.0.1",

)


app.include_router(entries.router)

app.mount("/", StaticFiles(directory="static/site", html= True), name="static")
