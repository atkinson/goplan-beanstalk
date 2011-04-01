"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright 2011 (atkinsonr@gmail.com / @tkinson)
"""

# Python

try:
    from xml.etree import cElementTree as ElementTree
except ImportError, e:
    from xml.etree import ElementTree

import urllib, urllib2


class Beanstalk(object):
    
    def __init__(self, accountname, username, password, *args, **kwargs):
        """ Instantiate an API object """
        self.accountname = accountname
        self.username = username
        self.password = password
        self.api_base = 'https://%s.beanstalkapp.com/api/' % self.accountname
        
    def repositories(self, repo=None, *args, **kwargs):
        """ Find all Repositories or a single repository by id or name"""

        """ URL depends on if one or all repos """
        if repo:
            url = urllib.basejoin(api_url, 'repositories.xml')
        else:
            url = urllib.basejoin(api_url, 'repositories/%s.xml' % repo)

        req = urllib2.urlopen(url).read()

        
        # rdata = []
        # chunk = 'xx'
        # while chunk:
        #     chunk = req.read()
        #     if chunk:
        #         rdata.append(chunk)
        # 
        # tree = ElementTree.fromstring(''.join(rdata))
        # results = []
        # for i, elem in enumerate(tree.getiterator('BookData')):
        #     results.append(
        #            {'isbn': elem.get('isbn'),
        #             'isbn13': elem.get('isbn13'),
        #             'title': elem.find('Title').text,
        #             'author': elem.find('AuthorsText').text,
        #             'publisher': elem.find('PublisherText').text,}
        #          )
        # return results