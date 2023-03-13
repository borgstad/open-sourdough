import os
from pathlib import Path

OPEN_SOURDOUGH_ROOT_IMAGE_DIR = Path(os.environ["OPEN_SOURDOUGH_ROOT_IMAGE_DIR"])
OPEN_SOURDOUGH_DB = {
    "host": os.environ["OPEN_SOURDOUGH_DB_HOST"],
    "db_name": os.environ["OPEN_SOURDOUGH_DB_NAME"],
    "user": os.environ["OPEN_SOURDOUGH_DB_USER"],
    "password": os.environ["OPEN_SOURDOUGH_DB_PASSWORD"],
    "port": os.environ["OPEN_SOURDOUGH_DB_PORT"],
}
