from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# staticフォルダを /static にマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    html = Path("static/index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)

@app.get("/api/echo")
async def echo(message: str):
    return {"message": message}
