import os

API_URL = "https://dados.mobilidade.rio/gps/brt"

CSV_FILE = "brt_data.csv"

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "postgres"),
    "database": os.getenv("POSTGRES_DB", "brt"),
    "user": os.getenv("POSTGRES_USER", "user"),
    "password": os.getenv("POSTGRES_PASSWORD", "password"),
    "port": 5432,
}
