from fastapi import requests
from fastapi import Request, FastAPI, Header, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .routers import hugs



templates = Jinja2Templates(directory="templates")


tags_metadata = [
    {
        "name": "hugs",
        "description": "The **hug** is _wonderful_.",
        "externalDocs": {
            "description": "Hugs external docs. Use to provide a link.",
            "url": "https://en.wikipedia.org/wiki/Hug",
        },
    },
  
]
app = FastAPI(
    openapi_tags=tags_metadata,
    title="The super duper Hugs API",
    description="This is an example for the base project Generator",
    version="v0.0.1",

)


app.include_router(hugs.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/my")
async def serve_my(request: Request):
    return templates.TemplateResponse("my.html", {"request": request})