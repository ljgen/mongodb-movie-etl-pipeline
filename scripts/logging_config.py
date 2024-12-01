import logging
import os

def setup_logging():
    # Configure logging:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=os.getenv("LOG_FILE"),
        filemode="a"
    )