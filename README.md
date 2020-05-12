# IReNE SearchSpace Server

The SearchSpace is a python-Flask application created to accomplish the needs of the User Interface of this service. The functions provided by this server are:
create a collaborator access request, retrieve the documents of the database to transfer them to the Front End, retrieve the possible options of filters in the database.
The retrieval of documents will depend of the service, different information of the documents is retrieved based on the service requested. For example: only metadata of the documents will
be transfer to the service, but all the information will be transferred when a request to get a single document is made. Also, between services like Map and Browse of the Front End have
different metadata transferred based on the needs of it.

## Getting Started

Following this instructions will let you work on your own files of the project for testing and/or develop features.

### Prerequisites
-Python3

Clone the repository to your machine with the following command:

```
git clone https://github.com/rubbertoe-G/IReNE-searchspace-ui.git
```


### Installing

To have this project up and running on your local machine, follow the next series of steps.

In the directory of the repository, create a virtual environment with Python
```
python3 -m venv ./venv
```
or in Windows 10
```
py -m venv ./venv
```

Activate the virtual environment.
```
source ./venv/bin/activate
```
or in Windows 10
```
./venv/Scripts/activate
```

Now install all the necessary requirements for the application server to run with the following command:
```
pip install -r requirements.txt
```

### Configuring the application
Before running the app, it's neede to set up the environment variables used in the initialization of the application
Create a new file called .env, follow this template to fill this file.
```
FLASK_APP=app
FLASK_ENV=development
# Use 1 for enable debug mode and 0 to disable it
FLASK_DEBUG=1

# Server host as NAME and PORt to use for use inside config
SERVER_NAME=NAME:PORT (ex. localhost:5000)

# Database
DB_NAME=<database-name>
DB_HOST=<your-database-connection-string>

# Authorization
GOOGLE_OAUTH_CLIENT_ID=<your-google-client-id>

```

### Running the application
To run the application server just execute the following command on the root directory and with the virtual environment activated.
```
python app.py
```
or in Windows 10
```
py app.py
```


## Testing

The testing performed to this application was endpoint testing, so as to confirm that the correct information was being given upon any request.
 In order to run the automatic tests, first you'll have to download [Postman](https://www.postman.com/downloads/).

### Import Postman Environment

In order to be able to use the tests developed, you will first need to import the created Postman Environment. 
This environment has all the necessary variables for the different requests to work. To import this environment, 
open up Postman and go to the settings wheel on the top right side of the user interface. Once pressed, 
a Manage Environment window should open. Press the import button and select the Postman environment
under the folder test in the repository called:
```
SearchSpace.Testing.postman_environment.json
```

These environment defines many components of the testing.

### Import Postman Collection

To import the test developed, open up Postman and press the Import button on the top left.
Select the collection file found in the test and import it. The name is:
```
SearchSpace.postman_collection.json
```


### Running the tests

Before running the tests, please make sure that you have successfully follow through the previous steps and that the application server is up and running.
 The following variables should exist on the Postman Environment in order to perform the tests correctly.
* url
* docid
* email
* first_name
* last_name
* gtoken

If Collaborator Request routes want to be tested it's needed to have a valid google token issued by google and for passing the test, this token has to be issued for the email of the 
collaborator to be created. Also the collaborator can't exist already.  
Once these steps are performed, go to the arrow inside the SearchSpace and press on the run button. A new window should pop up with all the test requests.
If the google token is not available unselect the collaborator related ones.
Press Run SearchSpace collection and all the requests will be sent to the server and the tests will be performed. 

## Documentation
In order to generate the documentation, run the following command on the root directory.
```
make html
```
or in Windows
```
.\make html
```
Go to Documentation\_build\html\index.html to see the generated documentation
## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide) - The web framework used
* [Sphinx](https://www.sphinx-doc.org/en/master/) - Used to generate documentation


## Authors

* **Alejandro Vasquez** - *Initial work* - [alejandroVasquez812](https://github.com/alejandroVasquez812)

See also the list of [contributors](https://github.com/rubbertoe-G/IReNE-searchspace-server/graphs/contributors) who participated in this project.
