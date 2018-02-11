#!/usr/bin/env bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

export FLASK_APP="autoapp.py"
export FLASK_DEBUG=0
export PYTHONPATH="$DIR"

while getopts "d" opt; do
  case $opt in
    d)
      FLASK_DEBUG=1
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

#export APP_CONFIG_FILE="$DIR/config/development.py"
#export APP_CONFIG="config/development.py"


source $(pipenv --venv)/bin/activate
#python manage.py runserver
#flask run
python -m flask run
