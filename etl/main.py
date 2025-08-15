# main.py
import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("ETL Job Started")

    raw_data = extract()
    if raw_data is None:
        logging.error("Extraction failed. Ending job.")
        return

    transformed_data = transform(raw_data)
    if transformed_data is None:
        logging.error("Transformation failed. Ending job.")
        return

    load(transformed_data)

    logging.info("ETL Job Finished")

if __name__ == "__main__":
    main()
