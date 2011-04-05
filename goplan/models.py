from django.db import models
from beanstalk.models import Repo

class Project(models.Model):
    """ A Goplan project """
    alias = models.CharField(max_length = 32, unique=True)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    archived = models.BooleanField()
    repo = models.ForeignKey(Repo, blank=True, null=True)

    def __unicode__(self):
        return self.name