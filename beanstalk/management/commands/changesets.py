import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import transaction

from beanstalk.api import Beanstalk
from beanstalk.models import Changeset, Repo, refresh_repositories

from goplan.api import GoPlanApi

class Command(BaseCommand):
    args = '<no args>'
    help = 'Check Beanstalk for Changesets'

    @transaction.commit_on_success
    def handle(self, *args, **options):
        beanstalk = Beanstalk(subdomain = settings.BEANSTALK_SUBDOMAIN,
                              username = settings.BEANSTALK_USERNAME,
                              password = settings.BEANSTALK_PASSWORD)
        
        changesets = beanstalk.get_changesets()
        
        for item in changesets:
            try:
                repo = Repo.objects.get(repo_id = item.get('repo_id'))
            except ObjectDoesNotExist:
                # Update repositories list, find the new repo
                refresh_repositories()
                repo = Repo.objects.get(repo_id = item.get('repo_id'))
                
            change, created = Changeset.objects.get_or_create(revision = item.get('revision'),
                                                              repo = repo )
            if created:
                change.message = item.get('message')
                change.author = item.get('author')
                change.email = item.get('email')
                change.save()
        
        start_time = datetime.datetime.now() - datetime.timedelta(minutes=1)
        end_time = datetime.datetime.now()
        new_changes = Changeset.objects.filter(
                        created__range=(
                            datetime.datetime.now()-datetime.timedelta(minutes=1),
                            end_time
                        ))
                        
        # There can be only one!
        user = User.objects.get(username=settings.OAUTH_KEY)
        profile = user.get_profile()
        goplan = GoPlanApi(company_alias = settings.GOPLAN_COMPANY_ALIAS,
                           consumer_key = settings.OAUTH_KEY,
                           consumer_secret = settings.OAUTH_SECRET,
                           oauth_token = profile.oauth_token,
                           oauth_secret = profile.oauth_secret)

        for change in new_changes:
            for ticket_id in change.get_related_tickets():
                print 'ticket: %s'%ticket_id
                message = '<a href="%s">Changeset %s</a> %s'%(change.get_absolute_url(), change.revision, change.message)
                
                try:
                    project = change.repo.project.get()
                    goplan.comment( project_alias = project.alias,
                                    item_type = 'ticket',
                                    item_id = ticket_id,
                                    message = message)
                except ObjectdoesNotExist:
                    # This repo is not associated with a project
                    pass

            for task_id in change.get_related_tasks():
                print 'task: %s'%task_id
                message = '<a href="%s">Changeset %s</a> %s'%(change.get_absolute_url(), change.revision, change.message)
                try:
                    project = change.repo.project.get()
                    goplan.comment( project_alias = project.alias,
                                    item_type = 'task',
                                    item_id = task_id,
                                    message = message)
                except ObjectdoesNotExist:
                    # This repo is not associated with a project
                    pass
