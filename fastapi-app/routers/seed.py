from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.products import ProductsService
from services.seed import SeedService

router = APIRouter()


@router.get("")
def run_seed(db: Session = Depends(get_db)):
    return SeedService.run_seed(db)
