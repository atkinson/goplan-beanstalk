# Python
import json

# Django
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response


from goplan.models import GoPlan
from goplan.api import GoPlanApi

def refresh_projects(request):
    """
    Get a list of projects from the GoPlan API and store them in the db
    """
    profile = request.user.get_profile()
    goplan = GoPlanApi(company_alias = settings.GOPLAN_COMPANY_ALIAS,
                    consumer_key = settings.OAUTH_KEY,
                    consumer_secret = settings.OAUTH_SECRET,
                    oauth_token = profile.oauth_token,
                    oauth_secret = profile.oauth_secret)

    item_list = goplan.enumerate_projects()
    for item in item_list:
         item = item.get('project')
         project, created = GoPlan.objects.get_or_create(alias=item.get('alias'))
         project.description = item.get('description')
         project.name = item.get('name')
         project.archived = item.get('archived')
         project.save()
    
    return HttpResponseRedirect(reverse('list_projects'))
    
def list_projects(request, template_name='list_projects.html'):
    ctx = {
        'project_list': GoPlan.objects.all()
    }
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))