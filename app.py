from create_app import create_app
'''
To run this server in development
    $ export FLASK_APP=`pwd`/app.py
    $ export FLASK_DEBUG=1
creating flask app instance

parameters could be
    config.development
    config.testing
    config.production
'''
# Search for the config file and add it to the
app = create_app('config.development')
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)