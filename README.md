# iPhone Data Analysis and REST API

This project is designed to analyze Apple iPhone product data, store it in a MySQL database, and provide a REST API built with FastAPI to access this data. It leverages Docker and Docker Compose to ensure that all application components are easily set up and managed within containers.

## Table of Contents

-   [Project Purpose](#project-purpose)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
-   [API Endpoints](#api-endpoints)
-   [Database Schema](#database-schema)
-   [Data Import Process](#data-import-process)
-   [Future Plans](#future-plans)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

## Project Purpose

The primary goals of this project are:

1.  **Data Management:** Clean and transform Apple iPhone product data from `apple_products.csv` and import it into a MySQL database.
2.  **API Development:** Develop a RESTful API (using FastAPI) to provide secure and flexible access to the stored product data.
3.  **Containerization:** Utilize Docker and Docker Compose to run the database and API services within isolated and portable containers.
4.  **Data Analysis Foundation:** Establish a solid foundation for more advanced data analysis and visualization in the future.

## Features

-   **Data Import:** Easy and fast data import from the `apple_products.csv` file into the database.
-   **REST API:** Access to product data with filtering options (`brand`, `ram`, `min_rating`, `max_price`).
-   **MySQL Database:** Relational data storage and querying.
-   **Docker & Docker Compose:** Quick setup and straightforward service management.
-   **Virtual Environment:** Isolated development environment for Python dependencies.

## Technologies Used

-   **Backend:**
    -   Python 3.11+
    -   [FastAPI](https://fastapi.tiangolo.com/)
    -   [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
    -   [Pydantic](https://pydantic-docs.helpmanual.io/) (Data validation and serialization)
    -   [python-dotenv](https://pypi.org/project/python-dotenv/) (Environment variables management)
-   **Database:**
    -   [MySQL 8.0](https://www.mysql.com/)
    -   [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) (MySQL connector)
-   **Data Processing:**
    -   [Pandas](https://pandas.pydata.org/)
-   **Containerization:**
    -   [Docker](https://www.docker.com/)
    -   [Docker Compose](https://docs.docker.com/compose/)

## Setup

### Prerequisites

To run this project, ensure you have the following software installed on your system:

-   [Git](https://git-scm.com/downloads)
-   [Docker Desktop](https://www.docker.com/products/docker-desktop) (includes Docker and Docker Compose)
-   [Python 3.11+](https://www.python.org/downloads/) (for setting up the virtual environment)

### Environment Variables

The project uses environment variables for sensitive information like database connection details. These variables are stored in a `.env` file, which is **not committed to the Git repository for security reasons**.

1.  **Copy the `.env.example` file:**
    Duplicate the `.env.example` file located in the project's root directory and rename the copy to `.env`.

    ```bash
    cp .env.example .env
    ```

2.  **Edit the `.env` file:**
    Open the newly created `.env` file with a text editor and fill in the following variables with your actual MySQL username and password.
    The `DB_HOST` value should remain `db`, as it refers to the MySQL service name within the Docker Compose network.

    ```dotenv
    # .env file (fill in your actual values after copying)

    DB_USER=yourcustomuser          # Enter your MySQL username here
    DB_PASS=your_strong_password    # Enter your MySQL password here (Choose a strong password!)
    DB_HOST=db                      # Docker Compose service name. Please do NOT change this value!
    DB_NAME=iphone_db               # The name of your database
    ```

### Running the Application

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/CosmicMass/iphone-analysis-api.git](https://github.com/CosmicMass/iphone-analysis-api.git)
    cd iphone-analysis-api
    ```

2.  **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv .venv
    # For Windows:
    .venv\Scripts\activate
    # For macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install Python Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start Docker Containers:**
    This command will spin up the MySQL database and FastAPI API services using Docker Compose in detached mode (in the background).

    ```bash
    docker-compose up --build -d
    ```
    -   `--build`: Rebuilds Docker images if there are changes.
    -   `-d`: Runs containers in detached (background) mode.

    **To ensure services are ready:** You can check the status of the services using `docker-compose ps` to see if they are in an `Up (healthy)` state. The MySQL database may take a little time to become `healthy`.

5.  **Import Data into the Database:**
    Once the application services are fully up and running, you can import the data from `apple_products.csv` into the MySQL database.

    ```bash
    python data_import.py
    ```
    This script will create the database tables if they don't exist and then import the data from the CSV file.

Your FastAPI API should now be running at `http://localhost:8000`!

## API Endpoints

The API is accessible at `http://localhost:8000`. For automatic API documentation, you can visit `/docs` (e.g., `http://localhost:8000/docs`).

### Listing and Filtering Products

-   **GET `/products`**
    -   Lists all iPhone products or filters them based on specific criteria.
    -   **Query Parameters:**
        -   `brand` (string, optional): Filters by brand (e.g., `Apple`).
        -   `ram` (string, optional): Filters by RAM size (e.g., `2 GB`, `4 GB`).
        -   `min_rating` (float, optional): Filters by minimum star rating (e.g., `4.5`).
        -   `max_price` (int, optional): Filters by maximum sale price (e.g., `60000`).

    **Example Requests:**

    ```
    GET http://localhost:8000/products
    GET http://localhost:8000/products?ram=2%20GB
    GET http://localhost:8000/products?min_rating=4.6&max_price=50000
    ```

## Database Schema

The `apple_products` table contains the following columns:

| Column Name           | Data Type   | Description                                           |
| :-------------------- | :---------- | :---------------------------------------------------- |
| `id`                  | `INTEGER`   | Primary key, auto-incrementing                        |
| `product_name`        | `VARCHAR`   | Full name of the product                              |
| `brand`               | `VARCHAR`   | Brand of the product (e.g., "Apple")                  |
| `sale_price`          | `INTEGER`   | Selling price of the product                          |
| `mrp`                 | `INTEGER`   | Maximum Retail Price                                  |
| `discount_percentage` | `INTEGER`   | Discount percentage                                   |
| `number_of_ratings`   | `INTEGER`   | Total number of ratings for the product               |
| `number_of_reviews`   | `INTEGER`   | Total number of reviews for the product               |
| `upc`                 | `VARCHAR`   | UPC (Universal Product Code) of the product           |
| `star_rating`         | `FLOAT`     | Average star rating of the product (between 0-5)      |
| `ram`                 | `VARCHAR`   | RAM size of the product (e.g., "2 GB", "4 GB")        |

## Data Import Process

The `data_import.py` script reads the `data/apple_products.csv` file, cleans missing values, converts data types, and performs a bulk insert operation into the `apple_products` table. This script is also responsible for creating the database tables (`Base.metadata.create_all`).

## Future Plans

This project aims to be extended with the following developments:

-   **Elasticsearch Integration:** Adding Elasticsearch and Kibana for powerful full-text search and advanced data analytics.
-   **More API Endpoints:** Implementing new API endpoints for analytical queries, such as average prices, top-rated products, or discount summaries.
-   **Frontend Development:** Building a frontend application (with React/Vue/Angular) to visualize the data from the API and provide an interactive user interface.
-   **AI-Powered Data Cleaning & Schema Suggestion:** Developing a system that leverages Large Language Models (LLMs) like Gemini to automatically suggest data cleaning steps, data types, and database schemas for various datasets.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License]. See the `LICENSE` file for more details.

## Contact

Mehmet Pala - mehmetapostrof@gmail.com

Project Link: [https://github.com/CosmicMass/iphone-analysis-api](https://github.com/CosmicMass/iphone-analysis-api)