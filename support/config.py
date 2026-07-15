import os
from dotenv import load_dotenv

# Load .env file into environment variables
load_dotenv()


def init_cofig():
    pass


def get_item(key, default=None):
    return os.getenv(key, default)
