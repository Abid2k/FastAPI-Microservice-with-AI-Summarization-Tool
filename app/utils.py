# app/utils.py
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_request(endpoint: str, data: dict):
    """Logs API request details."""
    logging.info(f"Request to {endpoint}: {data}")
