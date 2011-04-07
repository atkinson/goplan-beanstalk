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
    created = models.DateTimeField(auto_now_add=True)
    repo = models.ForeignKey(Repo)
    revision = models.CharField(max_length=40)
    message = models.TextField()
    author = models.CharField(max_length=36)
    email = models.CharField(max_length=128)

    
def refresh_repositories():
    """ Get a list of repos from the API and makes sure they are in the db """
    from django.conf import settings
    from beanstalk.api import Beanstalk
    
    beanstalk = Beanstalk(subdomain = settings.BEANSTALK_SUBDOMAIN,
                          username = settings.BEANSTALK_USERNAME,
                          password = settings.BEANSTALK_PASSWORD)

    repo_list = beanstalk.enumerate_repos()
    for item in repo_list:
        repo, created = Repo.objects.get_or_create(repo_id=item.get('id'))
        repo.repo_name = item.get('name')
        repo.repo_type =  item.get('type')
        repo.repo_title = item.get('title')
        repo.save()