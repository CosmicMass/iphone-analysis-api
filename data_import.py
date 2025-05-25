import pandas as pd
from app.db import engine, SessionLocal
from app.models import Base
from app.crud import create_products

# 1. Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

# 2. CSV oku
df = pd.read_csv("data/apple_products.csv")

# 2.1. Eksik değerleri doldur
df = df.fillna({
    "Sale Price": 0,
    "Mrp": 0,
    "Discount Percentage": 0,
    "Number Of Ratings": 0,
    "Number Of Reviews": 0,
    "Star Rating": 0,
    "Ram": "Unknown"
})

# 2.2. Tip dönüşümleri
df["Sale Price"] = df["Sale Price"].astype(int)
df["Mrp"] = df["Mrp"].astype(int)
df["Discount Percentage"] = df["Discount Percentage"].astype(int)
df["Number Of Ratings"] = df["Number Of Ratings"].astype(int)
df["Number Of Reviews"] = df["Number Of Reviews"].astype(int)
df["Star Rating"] = df["Star Rating"].astype(float)
df["Ram"] = df["Ram"].astype(str)

# 2.3. brand kolonunu ekle (tüm ürünler için "Apple")
df["brand"] = "Apple"

# 3. Kolon isimlerini değiştir ve dict listesine çevir
df = df.rename(columns={
    "Product Name": "product_name",
    "Sale Price": "sale_price",
    "Mrp": "mrp",
    "Discount Percentage": "discount_percentage",
    "Number Of Ratings": "number_of_ratings",
    "Number Of Reviews": "number_of_reviews",
    "Upc": "upc",
    "Star Rating": "star_rating",
    "Ram": "ram"
})

# Sadece modeldeki alanları bırak
model_fields = [
    "product_name", "brand", "sale_price", "mrp", "discount_percentage",
    "number_of_ratings", "number_of_reviews", "upc", "star_rating", "ram"
]
products = df[model_fields].to_dict(orient="records")
# 4. DB’ye aktar, hata varsa yakala
db = SessionLocal()
try:
    create_products(db, products)
except Exception as e:
    print("DB'ye aktarım hatası:", e)
finally:
    db.close()

# 5. Başarı Mesajı
print(f"{len(products)} kayıt veritabanına aktarıldı.")