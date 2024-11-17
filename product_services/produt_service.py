# app/product_services.py

from sqlalchemy.orm import Session
from product_services import crud, schemas

# Function to create a new category
def create_category(db: Session, category: schemas.CategoryCreate):
    return crud.create_category(db=db, category=category)

# Function to get a category by ID
def get_category(db: Session, category_id: int):
    return crud.get_category(db=db, category_id=category_id)

# Function to list categories with pagination
def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return crud.get_categories(db=db, skip=skip, limit=limit)

# Function to create a new product
def create_product(db: Session, product: schemas.ProductCreate):
    return crud.create_product(db=db, product=product)

# Function to get a product by ID
def get_product(db: Session, product_id: int):
    return crud.get_product(db=db, product_id=product_id)

# Function to list products with pagination
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return crud.get_products(db=db, skip=skip, limit=limit)

# Function to create a product variant
def create_product_variant(db: Session, variant: schemas.ProductVariantCreate, product_id: int):
    return crud.create_product_variant(db=db, variant=variant, product_id=product_id)

# Function to get product variants by product ID
def get_product_variants(db: Session, product_id: int):
    return crud.get_product_variants(db=db, product_id=product_id)
# get product details
def product_details_by_id(db:Session,id:int):
    return crud.get_product_by_id(db=db, id=id)

# Function to create a product image
def create_product_image(db: Session, image: schemas.ProductImageCreate, product_id: int):
    return crud.create_product_image(db=db, image=image, product_id=product_id)
