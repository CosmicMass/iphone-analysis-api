# app/db.py

from pathlib import Path
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Proje kökünü belirle
BASE_DIR = Path(__file__).parent.parent

# 2. .env dosyasının tam yolunu ver
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=dotenv_path)

# 3. Ortam değişkenlerini oku
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# 4. Hata ayıklamak için (geçici)
print(f"Loaded .env from {dotenv_path}")
print("DB_HOST:", DB_HOST, "| DB_USER:", DB_USER)

# 5. Connection URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
