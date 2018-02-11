#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# import sys
# import unittest
# import coverage
# from typing import Under
from app.app import create_app, db
from config.constants import ENVIRON_PREFIX

app = create_app(env=os.environ.get(ENVIRON_PREFIX + '_CONFIG'))


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db}

# if len(sys.argv) < 1:
#     raise AttributeError('Please provide an option')
#
# if sys.argv[1] not in ['runserver', 'test', 'coverage']:
#     raise AttributeError('Option not supported')
#
#
# if sys.argv[1] == 'runserver':
#     app = create_app()
#     app.run(host='0.0.0.0')

# if sys.argv[1] == 'test':
#     tests = unittest.TestLoader().discover('tests', pattern='*.py')
#     unittest.TextTestRunner(verbosity=1).run(tests)

# if sys.argv[1] == 'coverage':
#     cov = coverage.coverage(
#         branch=True,
#         include='project/*'
#     )
#     cov.start()
#     tests = unittest.TestLoader().discover('tests', pattern='*.py')
#     unittest.TextTestRunner(verbosity=2).run(tests)
#     cov.stop()
#     cov.save()
#     print('Coverage Summary:')
#     cov.report()
#     ROOT_PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
#     covdir = os.path.join(ROOT_PROJECT_DIR, 'coverage')
#     cov.html_report(directory=covdir)
#     cov.erase()
