from sqlalchemy.orm import Session
from .models import AppleProduct

def create_products(db: Session, products: list[dict]):
    objs = [AppleProduct(**p) for p in products]
    db.bulk_save_objects(objs)
    db.commit()
