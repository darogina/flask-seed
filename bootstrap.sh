#!/usr/bin/env bash

DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

FLASK_ENVS=('local' 'dev' 'prod')

FLASK_WSGI=0
FLASK_DEBUG=1
FLASK_ENV="${FLASK_APP_CONFIG}"
GUN_WORKERS="${GUN_WORKERS}"

while getopts "d:we:g:" opt; do
  case $opt in
    d)
      FLASK_DEBUG="${OPTARG}"
      ;;
    w)
      FLASK_WSGI=1
      ;;
    e)
      FLASK_ENV="$OPTARG"
      ;;
    g)
      GUN_WORKERS="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

containsElement () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

echo "FLASK_ENV: ${FLASK_ENV}"

if ! containsElement "$FLASK_ENV" "${FLASK_ENVS[@]}"; then
    echo "Please specify a valid Environment ('-e' or 'FLASK_APP_CONFIG' env var ) - Valid options: ${FLASK_ENVS[*]}"
    exit 1
fi

export FLASK_APP_CONFIG="$FLASK_ENV"

source $(pipenv --venv)/bin/activate

if [[ FLASK_WSGI -eq 1 ]]; then
    NUM_CORES=$(python -c 'import multiprocessing as mp; print(mp.cpu_count())')
    GUN_WORKERS_DEFAULT=$(( (2 * $NUM_CORES) + 1 )) # Taken from http://docs.gunicorn.org/en/stable/design.html#how-many-workers
    GUN_WORKERS=${GUN_WORKERS:=${GUN_WORKERS_DEFAULT}}
    echo "GUN_WORKERS: $GUN_WORKERS"
    gunicorn -w ${GUN_WORKERS:=2} -b 0.0.0.0:5000 wsgi:app
else
    export FLASK_APP="autoapp.py"
    # Debug should never be set for WSGI
    export FLASK_DEBUG=${FLASK_DEBUG}
    export PYTHONPATH="$DIR"

    python -m flask run
fi

