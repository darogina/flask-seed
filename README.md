# Flask Seed
Flask seed project...

## Quick Start

### Requirements

* Python 3
* Pipenv

### Setup
1. Install pipenv
    ```bash
    $ pip install pipenv
    ```
1. Create and activate virtual environment
    ```bash
    $ cd <project_dir>
    $ pipenv shell

    ```
1. Install python packages
    ```bash
    $ pipenv install
    ```
1. Set environment variables necessary to run Flask
    ```bash
    $ export FLASK_APP=autoapp.py
    $ export FLASK_APP_CONFIG=local
    ```
    > **NOTE**: You will need to set these two environment variables every time you re-activate the shell
1. Create local SQLite database
    ```bash
    $ flask db upgrade
    ```
1. Start the application
    ```bash
    $ flask run
    ```
1. Deactivate the shell
    ```bash
    $ exit
    ```