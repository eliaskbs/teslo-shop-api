import logging
import uuid as uuid_lib
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from models import Product, ProductImage
from schemas.product import CreateProduct, UpdateProduct

logger = logging.getLogger(__name__)


class ProductsService:
    @staticmethod
    def create(db: Session, data: CreateProduct) -> dict:
        try:
            images_data = data.images or []
            product_dict = data.model_dump(exclude={"images"})
            # Valores por defecto para no enviar None a la DB
            product_dict.setdefault("price", 0.0)
            product_dict.setdefault("stock", 0)
            product_dict.setdefault("tags", [])
            product_dict.setdefault("description", None)
            product_dict.setdefault("slug", None)
            product = Product(
                **product_dict,
                images=[ProductImage(url=url) for url in images_data],
            )
            db.add(product)
            db.commit()
            db.refresh(product)
            return ProductsService._to_plain(product)
        except Exception as e:
            db.rollback()
            ProductsService._handle_db_error(e)

    @staticmethod
    def find_all(db: Session, limit: int = 10, offset: int = 0) -> list[dict]:
        products = (
            db.query(Product)
            .options(joinedload(Product.images))
            .offset(offset)
            .limit(limit)
            .all()
        )
        return [ProductsService._to_plain(p) for p in products]

    @staticmethod
    def find_one(db: Session, term: str) -> Product | None:
        try:
            term_uuid = uuid_lib.UUID(term)
            product = (
                db.query(Product)
                .options(joinedload(Product.images))
                .filter(Product.id == term_uuid)
                .first()
            )
        except (ValueError, TypeError):
            product = (
                db.query(Product)
                .options(joinedload(Product.images))
                .filter(
                    or_(
                        Product.title.ilike(term),
                        Product.slug == term,
                    )
                )
                .first()
            )
        return product

    @staticmethod
    def find_one_plain(db: Session, term: str) -> dict:
        product = ProductsService.find_one(db, term)
        if not product:
            return None
        return ProductsService._to_plain(product)

    @staticmethod
    def update(db: Session, id: str, data: UpdateProduct) -> dict:
        product = ProductsService.find_one(db, id)
        if not product:
            return None

        update_data = data.model_dump(exclude_unset=True)
        images = update_data.pop("images", None)

        for key, value in update_data.items():
            setattr(product, key, value)

        if images is not None:
            # Eliminar imágenes actuales y crear nuevas
            db.query(ProductImage).filter(ProductImage.product_id == product.id).delete()
            product.images = [ProductImage(url=url) for url in images]

        try:
            db.commit()
            db.refresh(product)
            return ProductsService.find_one_plain(db, str(product.id))
        except Exception as e:
            db.rollback()
            ProductsService._handle_db_error(e)

    @staticmethod
    def remove(db: Session, id: str) -> bool:
        product = ProductsService.find_one(db, id)
        if not product:
            return False
        db.delete(product)
        db.commit()
        return True

    @staticmethod
    def remove_all(db: Session) -> None:
        db.query(ProductImage).delete()
        db.query(Product).delete()
        db.commit()

    @staticmethod
    def _to_plain(product: Product) -> dict:
        return {
            "id": product.id,
            "title": product.title,
            "price": product.price,
            "description": product.description,
            "slug": product.slug,
            "stock": product.stock,
            "sizes": product.sizes,
            "gender": product.gender,
            "tags": product.tags or [],
            "images": [img.url for img in (product.images or [])],
        }

    @staticmethod
    def _handle_db_error(error: Exception) -> None:
        if hasattr(error, "orig") and getattr(error.orig, "pgcode", None) == "23505":
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail="Duplicate key")
        logger.exception("Unexpected error")
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Unexpected error, check server logs")
