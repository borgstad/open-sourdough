import decouple
from pathlib import Path


OPEN_SOUR_DOUGH_REMOTE_IMAGE_DIR = decouple.config(
    "OPEN_SOUR_DOUGH_REMOTE_IMAGE_DIR", cast=Path
)
OPEN_SOUR_DOUGH_SSH_USERNAME = decouple.config("OPEN_SOUR_DOUGH_SSH_USERNAME", cast=str)
OPEN_SOUR_DOUGH_SSH_PORT = decouple.config("OPEN_SOUR_DOUGH_SSH_PORT", cast=int)
OPEN_SOUR_DOUGH_SSH_HOSTNAME = decouple.config("OPEN_SOUR_DOUGH_SSH_HOSTNAME", cast=str)
OPEN_SOUR_DOUGH_DB = {
    "default": {
        "HOST": decouple.config("OPEN_SOUR_DOUGH_DB_HOST"),
        "DB_NAME": decouple.config("OPEN_SOUR_DOUGH_DB_NAME"),
        "USER": decouple.config("OPEN_SOUR_DOUGH_DB_USER"),
        "PASSWORD": decouple.config("OPEN_SOUR_DOUGH_DB_PASSWORD"),
        "PORT": decouple.config("OPEN_SOUR_DOUGH_DB_PORT"),
    }
}
