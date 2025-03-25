
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

SUPPORTED_FORMATS = barcode.PROVIDED_BARCODES

def guess_format(data: str) -> str:
    if data.isnumeric() and len(data) == 13:
        return "ean13"
    elif data.isnumeric() and len(data) == 8:
        return "ean8"
    else:
        return "code128"  # Safe default for alphanumeric

def generate_barcode_image(data: str, fmt: str) -> BytesIO:
    if fmt not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {fmt}")
    
    barcode_class = barcode.get_barcode_class(fmt)
    buffer = BytesIO()
    barcode_obj = barcode_class(data, writer=ImageWriter())
    barcode_obj.write(buffer)
    buffer.seek(0)
    return buffer
