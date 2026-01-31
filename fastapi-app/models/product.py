import uuid
from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, event
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship

from database import Base


def slugify(value: str) -> str:
    if not value:
        return ""
    return value.lower().replace(" ", "_").replace("'", "")


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), unique=True, nullable=False)
    price = Column(Float, default=0.0)
    description = Column(Text, nullable=True)
    slug = Column(String(255), unique=True, nullable=False)
    stock = Column(Integer, default=0)
    sizes = Column(ARRAY(String), nullable=False)
    gender = Column(String(50), nullable=False)
    tags = Column(ARRAY(String), default=[])

    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product {self.title}>"


@event.listens_for(Product, "before_insert")
@event.listens_for(Product, "before_update")
def set_product_slug(mapper, connection, target):
    if not target.slug and target.title:
        target.slug = slugify(target.title)
    elif target.slug:
        target.slug = slugify(target.slug)


class ProductImage(Base):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id", ondelete="CASCADE"), nullable=False)

    product = relationship("Product", back_populates="images")

    def __repr__(self):
        return f"<ProductImage {self.url}>"
