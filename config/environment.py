from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
# APP
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
FLASK_DEBUG = os.getenv("FLASK_DEBUG")
SERVER_NAME = os.getenv("SERVER_NAME")

# Database
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv("DB_HOST")

# Google
GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
