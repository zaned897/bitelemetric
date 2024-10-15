from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_model=str)
async def home(request: Request)  -> templates.TemplateResponse:
    """ Home page """
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})

