import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

user = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
database = os.environ.get('DATABASE')
