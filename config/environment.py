from dotenv import load_dotenv
import os
""" Use a environment to set up the distinct parameters of the application"""
load_dotenv(verbose=True)
# APP
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")
# Use this is app.run will be empty like this app.run()
SERVER_NAME = os.getenv("SERVER_NAME")
# Use this to fill app.run arguments when use it like this app.run(host='HOST', port=PORT,)
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
# Select if the application will be on debug mode
FLASK_DEBUG = os.getenv("FLASK_DEBUG")

# Database
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv("DB_HOST")

# Google Client of the project to validate the token
GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
