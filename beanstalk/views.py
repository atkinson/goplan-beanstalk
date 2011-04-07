from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from beanstalk.models import refresh_repositories

def refresh_repos(request):
    """
    Get a list of repos from the Beanstalk API and store them in the db
    """
    refresh_repositories()    
    return HttpResponseRedirect(reverse('list_projects'))