from scripts.logging_config import setup_logging
import logging

# Set up logging
setup_logging()

def load_data(client, result):
    """Load Processed Data"""
    try:
        # Prepare processed data:
        processed_data = [
            {"genre": item["_id"], "avg_rating": item["avg_rating"], "lastUpdated": item["lastUpdated"]}
            for item in result
        ]

        # Ensure processed data is not empty:
        if not processed_data:
            logging.warning("No data to insert into processed_reports.")

            print("No data to insert into processed_reports.")
        else:
            # Reference the processed_data database:
            db_new = client["processed_data"]
            logging.info(f"Connected to database: {db_new.name}")

            proc_reports = db_new["processed_reports"]
            logging.info(f"Connected to collection: {proc_reports.name}")

            # Insert processed data
            proc_reports.insert_many(processed_data)
            logging.info("Processed data inserted into processed_reports collection.")

            print("Processed data inserted into processed_reports collection.")

    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        print(f"Error during data loading: {e}")
        exit(1)