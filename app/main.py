
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from app.barcode_logic import generate_barcode_image, guess_format
from io import BytesIO

app = FastAPI()

@app.get("/barcode")
def barcode_endpoint(
    data: str = Query(..., min_length=1),
    format: str | None = None,
):
    format_to_use = format or guess_format(data)
    try:
        image: BytesIO = generate_barcode_image(data, format_to_use)
        return StreamingResponse(image, media_type="image/png")
    except Exception as e:
        return {"error": str(e)}
