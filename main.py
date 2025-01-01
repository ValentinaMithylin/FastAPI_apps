from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("templates/index.html")


@app.get("/home", response_class=FileResponse)
async def read_home():
    return FileResponse("templates/home.html")