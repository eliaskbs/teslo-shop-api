from sqlalchemy.orm import Session

from services.products import ProductsService
from schemas.product import CreateProduct
from seed_data import initial_data


class SeedService:
    @staticmethod
    def run_seed(db: Session) -> str:
        ProductsService.remove_all(db)
        products = initial_data["products"]
        for product in products:
            payload = CreateProduct(
                title=product["title"],
                description=product["description"],
                images=product["images"],
                stock=product["stock"],
                price=product["price"],
                sizes=list(product["sizes"]),
                slug=product["slug"],
                tags=product["tags"],
                gender=product["gender"],
            )
            ProductsService.create(db, payload)
        return "SEED EXECUTE"
