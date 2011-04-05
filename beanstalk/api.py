"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright 2011 (atkinsonr@gmail.com / @tkinson)
"""

# Python
from xml.dom import minidom
import urllib, urllib2, base64

class Beanstalk(object):
    def __init__(self, subdomain, username, password):
        """ Instantiate an API object """
        self.api_base = 'https://%s.beanstalkapp.com/api/' % subdomain     
        self.basic_auth = 'Basic %s' %base64.encodestring('%s:%s' %(username, password)).replace('\n', '')

    def _open_url(self, url):
        request = urllib2.Request(url) 
        request.add_header("Authorization", self.basic_auth)
        return urllib2.urlopen(request).read()
    
    def _get_text(self, elt):
        if elt.firstChild:
            return elt.firstChild.data
        else:
            return ''
        
    def enumerate_repos(self):
        """ List all repositories"""
        url = urllib.basejoin(self.api_base, 'repositories.xml')
        req = self._open_url(url)
        dom = minidom.parseString(req)
        repos = dom.getElementsByTagName('repository')
        results = []
        for repo in repos:
            results.append({
                  'id': self._get_text(repo.getElementsByTagName('id')[0]),
                'name': self._get_text(repo.getElementsByTagName('name')[0]),
               'title': self._get_text(repo.getElementsByTagName('title')[0]),
                'type': self._get_text(repo.getElementsByTagName('type')[0])
            })
        return results

    def get_changesets(self):
        """ Get the last 15 changsets for al repos """
        url = urllib.basejoin(self.api_base, 'changesets.xml')
        req = self._open_url(url)
        dom = minidom.parseString(req)
        changesets = dom.getElementsByTagName('revision-cache')
        results = []
        for change in changesets:
            results.append({
               'repo_id': self._get_text(change.getElementsByTagName('repository-id')[0]),
              'revision': self._get_text(change.getElementsByTagName('revision')[0]),
               'message': self._get_text(change.getElementsByTagName('message')[0]),
                'author': self._get_text(change.getElementsByTagName('author')[0]),
                 'email': self._get_text(change.getElementsByTagName('email')[0])
            })
        return results

