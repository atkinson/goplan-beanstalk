from django.db import models

class Repo(models.Model):
    """ A beanstalk repo """
    repo_id = models.IntegerField(unique=True)
    repo_name = models.CharField(max_length = 64)
    repo_type = models.CharField(max_length = 32)
    repo_title = models.TextField(max_length = 128)

    def __unicode__(self):
        return self.repo_title
        
class Changeset(models.Model):
    """ A changeset in a repo """
    repo_id = models.ForeignKey(Repo)
    revision = models.CharField(max_length=40)
    message = models.TextField()
    author = models.CharField(max_length=36)
    email = models.CharField(max_length=128)
    