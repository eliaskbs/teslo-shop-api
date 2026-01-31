from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from config import settings
from helpers import file_filter, file_namer
from services.files import FilesService

router = APIRouter()

# Carpeta donde se guardan las subidas (relativa a la raíz del proyecto)
UPLOAD_PRODUCTS_DIR = Path(__file__).resolve().parent.parent.parent / "static" / "products"


@router.get("/product/{image_name}")
def get_product_image(image_name: str):
    return FilesService.send_product_image(image_name)


@router.post("/product")
async def upload_product_image(file: UploadFile = File(..., description="Image file (jpg, png, gif)")):
    if not file.content_type or not file_filter(file.content_type):
        raise HTTPException(
            status_code=400,
            detail="Make sure the file is a valid image (jpg, png, gif)",
        )
    UPLOAD_PRODUCTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = file_namer(file.filename or "image", file.content_type or "")
    path = UPLOAD_PRODUCTS_DIR / filename
    content = await file.read()
    path.write_bytes(content)
    secure_url = f"{settings.host_api}/api/files/product/{filename}"
    return {"fileName": secure_url}
