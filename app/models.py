from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AppleProduct(Base):
    __tablename__ = "apple_products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255))
    brand = Column(String(100))
    sale_price = Column(Integer)
    mrp = Column(Integer)
    discount_percentage = Column(Integer)
    number_of_ratings = Column(Integer)
    number_of_reviews = Column(Integer)
    upc = Column(String(100))
    star_rating = Column(Float)
    ram = Column(String(50))
