from scripts.logging_config import setup_logging
from pymongo import MongoClient
import logging
import os

# Set up logging
setup_logging()

def connect_to_mongodb():
    """Connect to MongoDB and return the client and database objects."""
    try:
        # Construct URI:
        uri = os.getenv("MONGO_URI")

        # Connect to MongoDb server:
        logging.info("Connecting to MongoDB server...")
        client = MongoClient(uri)

        print("Connecting to MongoDB server...")

        # Fetch database names:
        logging.info("Fetching list of databases...")
        dbs = client.list_database_names()
        logging.info(f"Available databases: {', '.join(dbs)}")

        print(f"Available databases: {', '.join(dbs)}")

        # Reference the sample_mflix database:
        db = client["sample_mflix"]
        logging.info(f"Connected to database: {db.name}")

        print(f"Connected to database: {db.name}")

        return client, db

    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        print(f"Error connecting to MongoDB: {e}")
        exit(1)

def close_connection(client):
    """Close the MongoDB connection."""
    try:
        logging.info("Closing the connection to the MongoDB server.")
        client.close()

        print("Closing the connection to the MongoDB server.")

    except Exception as e:
        logging.error(f"Error closing the MongoDB connection: {e}")
        print(f"Error closing the MongoDB connection: {e}")