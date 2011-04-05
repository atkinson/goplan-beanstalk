# Python
import json

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
        response, content = self.client.request('http://%s.goplanapp.com/api/projects/get_all?format=json'% self.company_alias)
        return json.loads(content)