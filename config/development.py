from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

DEBUG = os.getenv("DEBUG")
PREFIX_URL = os.getenv("PREFIX_URL")
DB = os.getenv("DB")


# Sessions
SECRET_KEY = os.getenv("SECRET_KEY")
SALT = os.getenv("SALT")