import os

from pathlib import Path
from dotenv import load_dotenv


ROOT = Path(__file__).parents[1]
ENV_FILE_PATH = str(ROOT / ".env")
ENV_PASSWORD_KEY = "SECRET_KEY"

load_dotenv(ENV_FILE_PATH)

PASSWORD = os.getenv(ENV_PASSWORD_KEY)
ENCODING = "utf-8"
ENCODE_EXT = 'enc'
DECODE_EXT = 'txt'
