from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class CreateProduct(BaseModel):
    title: str = Field(..., min_length=1)
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = None
    slug: Optional[str] = None
    stock: Optional[int] = Field(default=None, gt=0)
    sizes: list[str]
    gender: str = Field(..., pattern="^(men|women|woman|kid|unisex)$")
    tags: Optional[list[str]] = Field(default_factory=list)
    images: Optional[list[str]] = Field(default_factory=list)


class UpdateProduct(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = None
    slug: Optional[str] = None
    stock: Optional[int] = Field(default=None, gt=0)
    sizes: Optional[list[str]] = None
    gender: Optional[str] = Field(default=None, pattern="^(men|women|woman|kid|unisex)$")
    tags: Optional[list[str]] = None
    images: Optional[list[str]] = None


class ProductResponse(BaseModel):
    id: UUID
    title: str
    price: float
    description: Optional[str] = None
    slug: str
    stock: int
    sizes: list[str]
    gender: str
    tags: list[str]
    images: list[str]

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    id: UUID
    title: str
    price: float
    description: Optional[str] = None
    slug: str
    stock: int
    sizes: list[str]
    gender: str
    tags: list[str]
    images: list[str]

    class Config:
        from_attributes = True
