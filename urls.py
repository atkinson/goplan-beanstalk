from django.conf.urls.defaults import *
from django.contrib import admin
from extendedauth.views import oauth_login, oauth_logout, \
     oauth_authenticated
from goplan.views import refresh_projects, list_projects

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', oauth_login),
    url(r'^logout/?$', oauth_logout),
    url(r'^login/authenticated/?$', oauth_authenticated),
    url(r'^$', list_projects, name='list_projects'),
    url(r'^refresh$', refresh_projects, name='refresh_projects'),
)
