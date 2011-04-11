#!/bin/bash
PYTHONPATH="${PYTHONPATH}:/srv/goplan-beanstalk:/srv/goplan-beanstalk/virtualenv"
export PYTHONPATH
export DJANGO_SETTINGS_MODULE=settings

python /srv/goplan-beanstalk/manage.py changesets

