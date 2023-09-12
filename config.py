# - *- coding: utf- 8 - *-
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
USER = os.getenv('U')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
OPENAI_KEY = os.getenv('OPENAI_KEY')
BOT_ADMIN = []
