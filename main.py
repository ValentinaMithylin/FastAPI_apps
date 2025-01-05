from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("templates/index.html")


@app.get("/home", response_class=FileResponse)
async def read_home():
    return FileResponse("templates/home.html")


@app.get("/resume", response_class=FileResponse)
async def read_resume():
    return FileResponse("templates/resume.html")


@app.get("/portfolio", response_class=FileResponse)
async def read_portfolio():
    return FileResponse("templates/portfolio.html")


@app.get("/contact", response_class=FileResponse)
async def read_contact():
    return FileResponse("templates/contact.html")