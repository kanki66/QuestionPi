from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("homepage.html",{"request":request})

@general_pages_router.get("/allquestions/")
async def home(request: Request):
	return templates.TemplateResponse("allquestions.html",{"request":request})

@general_pages_router.get("/jquery/")
async def home(request: Request):
	return templates.TemplateResponse("jquery-1.7.1.min.js",{"request":request})