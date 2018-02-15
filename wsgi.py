import os

from app.app import create_app
from config.constants import ENVIRON_PREFIX

app = create_app(env=os.environ.get(ENVIRON_PREFIX + '_CONFIG'))