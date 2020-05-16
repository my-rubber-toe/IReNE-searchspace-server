"""
app.py
=======
Main file that runs the application.
"""
from create_app import ApiFlask

app = ApiFlask(__name__).create_app('config.environment')

if __name__ == '__main__':
    app.run(host='localhost', port=app.config['PORT'], debug=app.config['FLASK_DEBUG'])
