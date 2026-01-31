from pathlib import Path

from fastapi import HTTPException
from fastapi.responses import FileResponse

from config import settings

# Carpeta de imágenes de productos (relativa al proyecto raíz: teslo-shop)
STATIC_PRODUCTS_DIR = Path(__file__).resolve().parent.parent.parent / "static" / "products"


class FilesService:
    @staticmethod
    def get_static_product_image(image_name: str) -> Path:
        path = STATIC_PRODUCTS_DIR / image_name
        if not path.is_file():
            raise HTTPException(
                status_code=404,
                detail=f"Not product found with image {image_name}",
            )
        return path

    @staticmethod
    def send_product_image(image_name: str) -> FileResponse:
        path = FilesService.get_static_product_image(image_name)
        return FileResponse(path)
