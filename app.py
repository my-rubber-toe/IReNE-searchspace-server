from create_app import ApiFlask

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
if __name__ == '__main__':
    app = ApiFlask(__name__).create_app('config.environment')
    app.run()
