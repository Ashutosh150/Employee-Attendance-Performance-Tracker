import logging
import os

# Create logs directory if not exists
os.makedirs("logs", exist_ok=True)

# Configure the logger
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
