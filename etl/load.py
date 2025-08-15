# load.py
from sqlalchemy import create_engine
import logging
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_TABLE

def load(df):
    logging.info("Starting load to Postgres")
    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        df.to_sql(DB_TABLE, engine, if_exists="replace", index=False)
        logging.info(f"Data loaded successfully into table '{DB_TABLE}'")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
