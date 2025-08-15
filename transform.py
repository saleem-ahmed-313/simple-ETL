# transform.py
import pandas as pd
import logging

def transform(data):
    logging.info("Starting transformation")
    try:
        df = pd.DataFrame(data)
        df_simple = df[["id", "symbol", "name", "current_price", "market_cap"]].copy()
        df_simple["market_cap_millions"] = df_simple["market_cap"] / 1e6
        logging.info("Transformation successful")
        return df_simple
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return None
