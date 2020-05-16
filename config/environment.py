import os
""" Use a environment to set up the distinct parameters of the application"""
# APP
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")
FLASK_DEBUG=os.getenv("FLASK_DEBUG")

# Use this to fill app.run arguments when use it like this app.run(host='HOST', port=PORT,)
PORT = os.getenv("PORT")

# Database
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv("DB_HOST")

# Google Client of the project to validate the token
GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
