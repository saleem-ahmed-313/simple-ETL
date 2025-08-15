# config.py

# API Details
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
API_PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

# PostgreSQL Connection
DB_USER = "etl_user"
DB_PASS = "etl_pass"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "etl_db"
DB_TABLE = "crypto_simple"
