# Flask Seed
Flask seed project...

## Quick Start

### Requirements

* Python 3
* [Pipenv](https://docs.pipenv.org/)

### Basic Setup
1. Install pipenv
    ```sh
    $ pip install pipenv
    ```
1. Create and activate virtual environment
    ```sh
    $ cd <project_dir>
    $ pipenv shell
    ```
1. Install python packages
    ```sh
    $ pipenv install
    $ pipenv install --dev
    ```
### Set Environment Variables
Set environment variables necessary to run Flask. **NOTE**: This is only necessary if executing __flask__ directly and not through [bootstrap.sh](./bootstrap.sh).
```bash
$ export FLASK_APP=autoapp.py
$ export FLASK_APP_CONFIG=local
```
> **NOTE**: You will need to set these two environment variables every time you re-activate the shell

**_TODO_**: Implement something like python-dotenv
    
### Create DB
This will create an initial SQLite database based on latest migrations.
```sh
$ flask db upgrade
```

### Run the Application
A [bootstrap.sh](./bootstrap.sh) BASH script has been created to help run the application.

Local with debug mode:
```sh
$ ./bootstrap.sh -e local -d
```

Prod using [Gunicorn](http://gunicorn.org/)
```sh
$ ./bootstrap.sh -e prod -w
```

### Testing
Flask [click](http://flask.pocoo.org/docs/0.12/cli/#custom-commands) command (w/ coverage):
```sh
$ flask test
```

[Pytest](https://pytest.org/) without coverage:
```sh
$ pytest
```

[Pytest](https://pytest.org/) with coverage:
```sh
$ pytest --cov=app
```

### Deactivating an active python virtual environment
Assuming your current shell has an activate virtual environment (denoted by something similar to __(flask-seed-ETuCx1xA)__ within the shell), make sure to deactivate upon completion. 
```sh
$ exit
```

## Custom Flask commands
Various custom click commands have been defined within the [commands](./app/commands.py) module.
A full list of flask commands can be found by running...
```sh
$ flask --help

clean      Remove *.pyc and *.pyo files recursively starting at current directory.  
create_db  Create initial database.  
db         Perform database migrations.  
lint       Lint and check code style with flake8 and isort.  
run        Runs a development server.  
shell      Runs a shell in the app context.  
urls       Display all of the url matching routes for the project.  

$ flask urls
Rule               Endpoint
----------------------------------
/api/v1/expenses/  api.v1.expenses
/api/v1/incomes/   api.v1.incomes
```
