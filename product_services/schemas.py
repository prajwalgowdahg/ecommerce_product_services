# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional

# Category schema
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Product schema
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int
    category: CategoryResponse

    class Config:
        orm_mode = True


# Product variant schema
class ProductVariantBase(BaseModel):
    variant_name: str
    variant_value: str
    price: float
    stock: int

class ProductVariantCreate(ProductVariantBase):
    pass

class ProductVariantUpdate(ProductVariantBase):
    pass

class ProductVariantResponse(ProductVariantBase):
    id: int

    class Config:
        orm_mode = True


# Product Image schema
class ProductImageBase(BaseModel):
    image_url: str

class ProductImageCreate(ProductImageBase):
    pass

class ProductImageResponse(ProductImageBase):
    id: int

    class Config:
        orm_mode = True
class ProductReserveRequest(BaseModel):
     product_id: int
     quantity: int
