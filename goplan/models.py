from django.db import models

# Create your models here.
    
class Repo(models.Model):
    repo_id = models.CharField(max_length = 32, unique=True)
    repo_type = models.CharField(max_length = 32)
    repo_title = models.TextField(max_length = 128)

    def __unicode__(self):
        return self.repo_title
        

class GoPlan(models.Model):
    alias = models.CharField(max_length = 32, unique=True)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    repo = models.ForeignKey(Repo)

    def __unicode__(self):
        return self.name