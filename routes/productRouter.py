from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import *
from database import *
from typing import List

router = APIRouter(prefix='/products', tags=['PRODUCTS'])

@router.post("/", response_model=ProductRead, summary="Create a product")
def createProduct(*, session: Session = Depends(get_session), product: ProductCreate):
    db_product = Product.validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductRead], summary="Get all products")
def getProducts(*, session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products

@router.get("/{product_id}", response_model=ProductRead, summary="Get product by id")
def getProductByID(*, session: Session = Depends(get_session), product_id: int):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/{product_id}", summary="Delete product by id")
def deleteProductByID(*, session: Session = Depends(get_session), product_id: int):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product)
    session.commit()
    return {"ok": True}


