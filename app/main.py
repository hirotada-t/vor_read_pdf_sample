from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import pytesseract
from PIL import Image
import io
import csv

app = FastAPI()

# staticフォルダを /static にマウント
app.mount("/static", StaticFiles(directory="static"), name="static")
# outputフォルダを /output にマウント（CSVダウンロード用）
app.mount("/output", StaticFiles(directory="output"), name="output")

@app.get("/", response_class=HTMLResponse)
async def root():
    html = Path("static/index.html").read_text(encoding="utf-8")
    return HTMLResponse(html)

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    # 画像読み込み
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    # OCRでテキスト抽出
    text = pytesseract.image_to_string(image, lang='jpn')
    # CSVとして保存
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    csv_file = output_dir / f"{file.filename}.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in text.splitlines():
            writer.writerow([line])
    return {"text": text, "csv_path": f"output/{file.filename}.csv"}

@app.get("/api/echo")
async def echo(message: str):
    return {"message": message}