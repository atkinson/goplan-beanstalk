from django.conf import settings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from beanstalk.api import Beanstalk

def refresh_repos(request):
    """
    Get a list of repos from the Beanstalk API and store them in the db
    """
    beanstalk = Beanstalk(subdomain = settings.BEANSTALK_SUBDOMAIN,
                          username = settings.BEANSTALK_USERNAME,
                          password = settings.BEANSTALK_PASSWORD)

    item_list = beanstalk.enumerate_repos()
    print item_list
    
    return HttpResponseRedirect(reverse('list_projects'))