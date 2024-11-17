# app/main.py

from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from product_services import crud, schemas, models, database
from product_services import produt_service
from product_services.database import get_db
from product_services.crud import reserve_product_service


app = FastAPI()


# Create the tables in the database
models.Base.metadata.create_all(bind=database.engine)


@app.post("/categories/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return produt_service.create_category(db=db, category=category)


@app.get("/categories/", response_model=List[schemas.CategoryResponse])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return produt_service.get_categories(db=db, skip=skip, limit=limit)


@app.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return produt_service.create_product(db=db, product=product)


@app.get("/products/", response_model=List[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return produt_service.get_products(db=db, skip=skip, limit=limit)

@app.get("/products/{id}")
def product_details(id:int,db: Session = Depends(get_db)):
    return produt_service.product_details_by_id(db=db,id=id)

@app.post("/products/reserve", response_model=schemas.ProductReserveRequest)
def reserve_product(
    reserve_request: schemas.ProductReserveRequest, db: Session = Depends(get_db)
):
    """
    API endpoint to reserve a product by reducing its stock.
    Delegates logic to the service layer.
    """
    try:
        product = reserve_product_service(reserve_request, db)
        print(product,flush=True)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))