from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from schemas.product import CreateProduct, UpdateProduct
from services.products import ProductsService

router = APIRouter()


@router.post("", response_model=dict)
def create_product(
    data: CreateProduct,
    db: Session = Depends(get_db),
):
    return ProductsService.create(db, data)


@router.get("", response_model=list)
def get_products(
    limit: int = Query(default=10, gt=0),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    return ProductsService.find_all(db, limit=limit, offset=offset)


@router.get("/{term}", response_model=dict)
def get_product(
    term: str,
    db: Session = Depends(get_db),
):
    result = ProductsService.find_one_plain(db, term)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Product with id {term} not found")
    return result


@router.patch("/{id}", response_model=dict)
def update_product(
    id: str,
    data: UpdateProduct,
    db: Session = Depends(get_db),
):
    result = ProductsService.update(db, id, data)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Product with id {id} not found")
    return result


@router.delete("/{id}", status_code=204)
def delete_product(
    id: str,
    db: Session = Depends(get_db),
):
    if not ProductsService.remove(db, id):
        raise HTTPException(status_code=404, detail=f"Product with id {id} not found")
    return None
