from fastapi import FastAPI, UploadFile, File, Response
from fastapi.responses import StreamingResponse, FileResponse
from outline import stroke
from PIL import Image
import io

app = FastAPI()


@app.post("/outline")
async def image_outline(file: UploadFile = File(...), stroke_size: int = 10):
    img = stroke(Image.open(file.filename), threshold=0, stroke_size=stroke_size, colors=((255, 255, 255),))
    image_bytes = io.BytesIO()
    img.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    return StreamingResponse(image_bytes, media_type="image/png")
