"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright 2011 (atkinsonr@gmail.com / @tkinson)
"""

# Python
import json, urllib

# External Libs
import oauth2 as oauth


class GoPlanApi(object):
    def __init__(self, company_alias, consumer_key, consumer_secret, oauth_token, oauth_secret):
        """
        company_alias refers to: http://company_alias.goplanapp.com/
        consumer_key and consumer_secret are created by registering an app on dev.goplanapp.com
        oauth_token and oauth_secret are returned from oauth authorization.
        """
        token = oauth.Token(oauth_token,oauth_secret)
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        self.client = oauth.Client(consumer, token)
        self.company_alias = company_alias
        
    def enumerate_projects(self):
        """
        Query remote GoPlan for a list of projects
        For each project, get or create a model
        Return a queryset of these
        """
        response, content = self.client.request(
                    'http://%s.goplanapp.com/api/projects/get_all?format=json'% self.company_alias)
        return json.loads(content)
        
        
        
    def comment(self, project_alias, item_type, item_id, message):
        """
        Update the task with a comment derived from the changeset message.
        """
        safe_message = urllib.quote(message)
        response, content = self.client.request(
            'http://%s.goplanapp.com/%s/api/comments/create?&comment[commentable_type]=%s&comment[commentable_cid]=%s&comment[text]=%s' \
            %(self.company_alias, project_alias, item_type, item_id, safe_message))