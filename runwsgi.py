import os, sys

PROJECT_ROOT = os.path.dirname(__file__)

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "virtualenv"))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['P46ISPROD'] = 'True'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

