"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright 2011 (atkinsonr@gmail.com / @tkinson)
"""

from django.db import models
from beanstalk.models import Repo

class Project(models.Model):
    """ A Goplan project """
    alias = models.CharField(max_length = 32, unique=True)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    archived = models.BooleanField()
    repo = models.ForeignKey(Repo, blank=True, null=True, related_name='project')

    def __unicode__(self):
        return self.name