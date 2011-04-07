import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from beanstalk.api import Beanstalk
from beanstalk.models import Changeset, Repo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Check Beanstalk for Changesets'

    def handle(self, *args, **options):
        beanstalk = Beanstalk(subdomain = settings.BEANSTALK_SUBDOMAIN,
                              username = settings.BEANSTALK_USERNAME,
                              password = settings.BEANSTALK_PASSWORD)
        
        changesets = beanstalk.get_changesets()
        
        for item in changesets:
            try:
                repo = Repo.objects.get(repo_id = item.get('repo_id'))
            except ObjectDoesNotExist:
                # TODO: Update repositories list and get new repo
                pass
                
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
        for change in new_changes:
            print change.message