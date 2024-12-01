from scripts.logging_config import setup_logging
import logging

# Set up logging
setup_logging()

def extract_data(db):
    """Extract Data"""
    try:
        movies = db["movies"]
        logging.info(f"Connected to collection: {movies.name}")

        print(f"Connected to collection: {movies.name}")

        return movies

    except Exception as e:
        logging.error(f"Error accessing collections: {e}")
        print(f"Error accessing collections: {e}")
        exit(1)