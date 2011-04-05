# Python
import json

# Django
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory

from django.contrib.auth.decorators import login_required

from goplan.models import Project
from goplan.forms import ProjectForm
from goplan.api import GoPlanApi
from beanstalk.models import Repo

def list_projects(request, template_name='list_projects.html'):
    ProjectFormSet = modelformset_factory(Project, ProjectForm, extra=0)
    ctx = {}
    if request.method == "POST":
        formset = ProjectFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            ctx.update({'message': 'Your changes have been saved!'})
    else:
        formset = ProjectFormSet()

    ctx.update({'formset': formset})
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
@login_required
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
         project, created = Project.objects.get_or_create(alias=item.get('alias'))
         project.description = item.get('description')
         project.name = item.get('name')
         project.archived = item.get('archived')
         project.save()
    
    return HttpResponseRedirect(reverse('list_projects'))
