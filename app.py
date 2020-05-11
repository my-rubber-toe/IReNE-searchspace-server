"""
app.py
=======
Main file that runs the application.
"""
from create_app import ApiFlask
# Search for the config file and add it to the app
if __name__ == '__main__':
    app = ApiFlask(__name__).create_app('config.environment')
    app.run()
