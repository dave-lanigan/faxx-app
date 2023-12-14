from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx, htmx_init
from jinjax import Catalog

app = FastAPI()

catalog = Catalog()
catalog.add_folder("app/components")

htmx_init(templates=Jinja2Templates(directory=Path("app") / "templates"))

@app.get("/", response_class=HTMLResponse)
#@htmx("index", "index")
async def index(request: Request):
    #return {"greeting": "Hello World"}
    return catalog.render("Layout", title="Hello world", __content="TEST")

@app.get("/customers", response_class=HTMLResponse)
@htmx("customers")
async def get_customers(request: Request):
    return {"customers": ["John Doe", "Jane Doe"]}