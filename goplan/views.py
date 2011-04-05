# Python
import json

# Django
from django.conf import settings
from django.http import HttpResponse


# Libs
from goplan import GoPlan

def mappings(request):
    profile = request.user.get_profile()
    goplan = GoPlan(company_alias = settings.GOPLAN_COMPANY_ALIAS,
                    consumer_key = settings.OAUTH_KEY,
                    consumer_secret = settings.OAUTH_SECRET,
                    oauth_token = profile.oauth_token,
                    oauth_secret = profile.oauth_secret)

    project_list = goplan.enumerate_projects()
    
    return HttpResponse(project_list, mimetype='text/plain')