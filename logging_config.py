
# logging_config.py - Logging Setup for Database Security Testing Tool

import logging

# Configure logging settings
def setup_logging(log_file="db_security_tool.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging setup complete.")

# Example usage in a module
if __name__ == "__main__":
    setup_logging()
    logging.info("This is an info message for testing.")
    logging.warning("This is a warning message for testing.")
    logging.error("This is an error message for testing.")
