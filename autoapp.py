#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from app.app import create_app, db
from config.constants import ENVIRON_PREFIX

app = create_app(env=os.environ.get(ENVIRON_PREFIX + '_CONFIG'))


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db}
