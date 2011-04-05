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
        
    def enumerate_repos(self):
        """ List all repositories"""
        url = urllib.basejoin(self.api_base, 'repositories.xml')
        req = self._open_url(url)
        dom = minidom.parseString(req)
        repos = dom.getElementsByTagName('repository')
        results = []
        for repo in repos:
            results.append({
                  'id': repo.getElementsByTagName('id')[0].firstChild.data,
                'name': repo.getElementsByTagName('name')[0].firstChild.data,
               'title': repo.getElementsByTagName('title')[0].firstChild.data,
                'type': repo.getElementsByTagName('type')[0].firstChild.data
            })
        return results

    def get_repo(self, repo):
        url = urllib.basejoin(self.api_base, 'repositories/%s.xml' % repo)
        req = self._open_url(url)

