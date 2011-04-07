"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright 2011 (atkinsonr@gmail.com / @tkinson)
"""

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