# app/crud.py

from sqlalchemy.orm import Session
from product_services import models, schemas
from product_services.schemas import ProductReserveRequest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
# CRUD for Categories
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()


# CRUD for Products
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        category_id=product.category_id
    )
    print(db_product,"checkthisout")
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


# CRUD for Product Variants
def create_product_variant(db: Session, variant: schemas.ProductVariantCreate, product_id: int):
    db_variant = models.ProductVariant(
        product_id=product_id,
        variant_name=variant.variant_name,
        variant_value=variant.variant_value,
        price=variant.price,
        stock=variant.stock
    )
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant

def get_product_variants(db: Session, product_id: int):
    return db.query(models.ProductVariant).filter(models.ProductVariant.product_id == product_id).all()
def get_product_by_id(db:Session,id:int):
    return db.query(models.Product).filter(models.Product.id==id).first()


# CRUD for Product Images
def create_product_image(db: Session, image: schemas.ProductImageCreate, product_id: int):
    db_image = models.ProductImage(image_url=image.image_url, product_id=product_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def reserve_product_service(reserve_request: ProductReserveRequest, db: Session) -> schemas.ProductReserveRequest:
    """
    Service layer logic for reserving a product.
    Reduces stock by the requested amount if available.
    """
    product = db.query(models.Product).filter(models.Product.id == reserve_request.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < reserve_request.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    # Update the stock and save
    product.stock -= reserve_request.quantity
    db.add(product)
    db.commit()
    db.refresh(product)
    print(product.id,"this product",flush=True)
    return schemas.ProductReserveRequest(
        product_id=product.id,
        quantity=product.stock,
    )