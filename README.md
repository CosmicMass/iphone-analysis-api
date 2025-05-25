# iPhone Veri Analizi ve REST API

Bu proje, Apple iPhone ürün verilerini analiz etmek, bir MySQL veritabanında depolamak ve bu verilere erişmek için bir FastAPI tabanlı REST API sunmak üzere tasarlanmıştır. Ayrıca, Docker ve Docker Compose kullanarak tüm uygulama bileşenlerinin kolayca kurulabilir ve yönetilebilir olmasını sağlar. İlerleyen aşamalarda Elasticsearch entegrasyonu ve bir frontend görselleştirme katmanı eklenmesi hedeflenmektedir.

## İçindekiler

- [Proje Amacı](#proje-amacı)
- [Özellikler](#özellikler)
- [Teknolojiler](#teknolojiler)
- [Kurulum](#kurulum)
  - [Önkoşullar](#önkoşullar)
  - [Ortam Değişkenleri](#ortam-değişkenleri)
  - [Uygulamayı Çalıştırma](#uygulamayı-çalıştırma)
- [API Uç Noktaları](#api-uç-noktaları)
- [Veritabanı Yapısı](#veritabanı-yapısı)
- [Veri İmport İşlemi](#veri-import-işlemi)
- [Gelecek Planları](#gelecek-planları)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [İletişim](#iletişim)

## Proje Amacı

Bu projenin temel amaçları şunlardır:

1.  **Veri Yönetimi:** `apple_products.csv` dosyasındaki iPhone ürün verilerini temizleyip dönüştürerek bir MySQL veritabanına aktarmak.
2.  **API Geliştirme:** Depolanan ürün verilerine güvenli ve esnek bir şekilde erişim sağlayan bir RESTful API (FastAPI ile) geliştirmek.
3.  **Konteynerleştirme:** Docker ve Docker Compose kullanarak veritabanı ve API servislerini izole ve taşınabilir konteynerler içinde çalıştırmak.
4.  **Veri Analizi Altyapısı:** İleride daha gelişmiş veri analizleri ve görselleştirmeler için bir temel oluşturmak.

## Özellikler

-   **Veri İmportu:** `apple_products.csv` dosyasından veritabanına kolay veri aktarımı.
-   **REST API:** Ürün verilerine filtreleme seçenekleriyle (`brand`, `ram`, `min_rating`, `max_price`) erişim.
-   **MySQL Veritabanı:** İlişkisel veri depolama.
-   **Docker & Docker Compose:** Hızlı kurulum ve kolay servis yönetimi.
-   **Sanal Ortam:** Python bağımlılıkları için izole geliştirme ortamı.

## Teknolojiler

-   **Backend:**
    -   Python 3.11+
    -   [FastAPI](https://fastapi.tiangolo.com/)
    -   [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
    -   [Pydantic](https://pydantic-docs.helpmanual.io/) (Veri doğrulama ve seri hale getirme)
    -   [python-dotenv](https://pypi.org/project/python-dotenv/) (Ortam değişkenleri yönetimi)
-   **Veritabanı:**
    -   [MySQL 8.0](https://www.mysql.com/)
    -   [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) (MySQL bağlantısı)
-   **Veri İşleme:**
    -   [Pandas](https://pandas.pydata.org/)
-   **Konteynerleştirme:**
    -   [Docker](https://www.docker.com/)
    -   [Docker Compose](https://docs.docker.com/compose/)

## Kurulum

### Önkoşullar

Projenizi çalıştırmak için aşağıdaki yazılımların sisteminizde yüklü olması gerekmektedir:

-   [Git](https://git-scm.com/downloads)
-   [Docker Desktop](https://www.docker.com/products/docker-desktop) (Docker ve Docker Compose'u içerir)
-   [Python 3.11+](https://www.python.org/downloads/) (Sanal ortam kurmak için)

### Ortam Değişkenleri

Proje, veritabanı bağlantı bilgileri için ortam değişkenlerini kullanır. Projenizin kök dizininde `.env` adında bir dosya oluşturmanız ve aşağıdaki formatta doldurmanız gerekmektedir:

```dotenv
# .env dosyası

DB_USER=your_mysql_user
DB_PASS=your_mysql_password
DB_HOST=db  # Docker Compose network içinde servis adı
DB_NAME=your_database_name