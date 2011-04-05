from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from beanstalk.api import Beanstalk
from beanstalk.models import Repo

def refresh_repos(request):
    """
    Get a list of repos from the Beanstalk API and store them in the db
    """
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
    
    return HttpResponseRedirect(reverse('list_projects'))