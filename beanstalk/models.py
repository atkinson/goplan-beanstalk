from django.db import models

class Repo(models.Model):
    """ A beanstalk repo """
    repo_id = models.CharField(max_length = 32, unique=True)
    repo_name = models.CharField(max_length = 64)
    repo_type = models.CharField(max_length = 32)
    repo_title = models.TextField(max_length = 128)

    def __unicode__(self):
        return self.repo_title