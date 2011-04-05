from django.conf.urls.defaults import *
from django.contrib import admin
from extendedauth.views import oauth_login, oauth_logout, \
     oauth_authenticated
from goplan.views import mappings as goplan_mappings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', oauth_login),
    url(r'^logout/?$', oauth_logout),
    url(r'^login/authenticated/?$', oauth_authenticated),
    url(r'^$', goplan_mappings)
)
