import re
from django.db import models
from django.conf import settings

class Repo(models.Model):
    """ A beanstalk repo """
    repo_id = models.IntegerField(unique=True)
    repo_name = models.CharField(max_length = 64)
    repo_type = models.CharField(max_length = 32)
    repo_title = models.TextField(max_length = 128)

    def __unicode__(self):
        return self.repo_name
        
    def get_absolute_url(self):
        """ This is the Beanstalk URL of the repo """
        return 'https://%s.beanstalkapp.com/%s/'%(settings.BEANSTALK_SUBDOMAIN, self.repo_name)

        
class Changeset(models.Model):
    """ A changeset in a repo """
    created = models.DateTimeField(auto_now_add=True)
    repo = models.ForeignKey(Repo)
    revision = models.CharField(max_length=40)
    message = models.TextField()
    author = models.CharField(max_length=36)
    email = models.CharField(max_length=128)

    def __unicode__(self):
        return '[%s %s] %s'%(self.repo, self.revision, self.message)

    def get_absolute_url(self):
        """ This is the beanstalk URL of the changeset """
        return 'https://%s.beanstalkapp.com/%s/changesets/%s'%(settings.BEANSTALK_SUBDOMAIN, self.repo, self.revision)
        
    def get_related_tasks(self):
        """ Returns a list of strings that match the task pattern eg: task22 returns ['22'] """
        tasks = re.findall(r'task[0-9+]*', self.message)
        return [task.strip('task') for task in tasks]
    
    def get_related_tickets(self):
        """ Returns a list of strings that match the ticket pattern eg: ticket22 returns ['22'] """
        tickets = re.findall(r'ticket[0-9+]*', self.message)
        return [ticket.strip('ticket') for ticket in tickets]
        
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