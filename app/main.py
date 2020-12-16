from .routers import pat_records
from fastapi import requests
from fastapi import Request, FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


tags_metadata = [
    {
        "name": "Records",
        "description": "API to interact with PAT API data",
        "externalDocs": {
            "description": "PAT project site.",
            "url": "https://aka.ms/pathack",
        },
    },
  
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="PAT Records API",
    description="This is an example for the base project Generator",
    version="v0.0.1",

)


app.include_router(pat_records.router)

app.mount("/", StaticFiles(directory="static/site", html= True), name="static")
