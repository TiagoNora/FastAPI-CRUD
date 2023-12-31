from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from models import *
from database import *
from typing import List

router = APIRouter(prefix='/products', tags=['PRODUCTS'])

@router.post("/", response_model=ProductRead, summary="Create a product")
def createProduct(*, session: Session = Depends(get_session), product: ProductCreate):
    db_product = Product.model_dump(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductRead], summary="Get all products")
def getProducts(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, le=100)):
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
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

@router.patch("/{product_id}", response_model=ProductRead)
def update_hero(product_id: int, product: ProductUpdate):
    with Session(engine) as session:
        db_product = session.get(Product, product_id)
        if not db_product:
            raise HTTPException(status_code=404, detail="Product not found")
        product_data = product.model_dump(exclude_unset=True)
        for key, value in product_data.items():
            setattr(db_product, key, value)
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        return db_product

