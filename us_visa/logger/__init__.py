import logging
import os
from datetime import datetime
from from_root import from_root  # তোমার project root path function

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_dir = 'logs'

# শুধু directory path বানাও
logs_dir_path = os.path.join(from_root(), log_dir)
os.makedirs(logs_dir_path, exist_ok=True)

# ফাইল path বানাও
logs_path = os.path.join(logs_dir_path, LOG_FILE)

logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging.info("Logger setup complete")
