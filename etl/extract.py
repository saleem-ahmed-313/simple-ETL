# extract.py
import requests
import logging
from config import API_URL, API_PARAMS

def extract():
    logging.info("Starting data extraction from API")
    try:
        resp = requests.get(API_URL, params=API_PARAMS, timeout=10)
        resp.raise_for_status()
        logging.info("Data extraction successful")
        return resp.json()
    except Exception as e:
        logging.error(f"Error extracting data: {e}")
        return None
