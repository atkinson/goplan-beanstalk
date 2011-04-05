from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from beanstalk.api import Beanstalk

class Command(BaseCommand):
    args = '<no args>'
    help = 'Check Beanstalk for Changesets'

    def handle(self, *args, **options):
        beanstalk = Beanstalk(subdomain = settings.BEANSTALK_SUBDOMAIN,
                              username = settings.BEANSTALK_USERNAME,
                              password = settings.BEANSTALK_PASSWORD)
        
        changesets = beanstalk.get_changesets()
        print changesets
