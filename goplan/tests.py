"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from django.conf import settings
from goplan.api import GoPlanApi

class GoPlanTests(TestCase):
    def test_comment(self):
        """
        Comment on Ticket 1.
        """
        profile = User.objects.order_by('last_login')[0].get_profile()
        goplan = GoPlanApi(company_alias = settings.GOPLAN_COMPANY_ALIAS,
                        consumer_key = settings.OAUTH_KEY,
                        consumer_secret = settings.OAUTH_SECRET,
                        oauth_token = profile.oauth_token,
                        oauth_secret = profile.oauth_secret)

        message = 'Changeset <a href="%s">%s</a> %s'%('http://example.com/', '101010', 'This is a test message')
        goplan.comment( project_alias = 'healthcraft',
                        item_type = 'ticket',
                        item_id = '1',
                        message = message)

