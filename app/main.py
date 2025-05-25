# app/main.py

from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db import SessionLocal, engine
from app.models import Base, AppleProduct
from pydantic import BaseModel

# Eğer henüz tabloları oluşturmamışsan, uncomment et:
Base.metadata.create_all(bind=engine)

app = FastAPI(title="iPhone Analysis API", debug=True)

# ----- Pydantic Schemas -----
class ProductRead(BaseModel):
    id: int
    product_name: str
    brand: Optional[str]
    sale_price: Optional[int]
    mrp: Optional[int]
    discount_percentage: Optional[int]
    number_of_ratings: Optional[int]
    number_of_reviews: Optional[int]
    upc: Optional[str]
    star_rating: Optional[float]
    ram: Optional[str]

    class Config:
        orm_mode = True

# ----- Dependency -----
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- Endpoints -----
@app.get("/products", response_model=List[ProductRead])
def list_products(
    brand: Optional[str] = Query(None, description="Filtre: brand eşitlik"),
    ram: Optional[str] = Query(None, description="Filtre: ram eşitlik"),
    min_rating: Optional[float] = Query(None, ge=0, le=5, description="Filtre: star_rating >= min_rating"),
    max_price: Optional[int]   = Query(None, ge=0, description="Filtre: sale_price <= max_price"),
    db: Session = Depends(get_db)
):
    query = db.query(AppleProduct)

    if brand:
        query = query.filter(AppleProduct.brand == brand)
    if ram:
        query = query.filter(AppleProduct.ram == ram)
    if min_rating is not None:
        query = query.filter(AppleProduct.star_rating >= min_rating)
    if max_price is not None:
        query = query.filter(AppleProduct.sale_price <= max_price)

    return query.all()
