# Dockerfile

FROM python:3.11-slim

# Ortam değişkenleri
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Gerekli dizine geç
WORKDIR /code

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Default olarak FastAPI başlatılacak
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
