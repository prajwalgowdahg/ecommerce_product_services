# app/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from product_services.database import Base

# Category model
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)  # Ensure this field exists
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship("Category", back_populates="products")
    
    # Define relationships for variants and images
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")


# Product Variant model (for different versions of the product like size, color, etc.)
class ProductVariant(Base):
    __tablename__ = "product_variants"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    variant_name = Column(String)  # E.g., "Size", "Color"
    variant_value = Column(String)  # E.g., "Large", "Red"
    price = Column(Float)
    stock = Column(Integer)

    product = relationship("Product", back_populates="variants")


# Product Image model (for storing multiple images)
class ProductImage(Base):
    __tablename__ = "product_images"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    image_url = Column(String)  # URL or path to the image

    product = relationship("Product", back_populates="images")
