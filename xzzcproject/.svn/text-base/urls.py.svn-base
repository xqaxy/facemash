from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin

import urllib
import time
import sys
import MySQLdb
from setupdb import *
import settings
from gallery.views import top
from gallery.views import browse
from gallery.views import vote
from gallery.views import detail
from gallery.views import index

# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^xzzcproject/', include('xzzcproject.foo.urls')),
    # url(r'^setup/', setup),

    url(r'^top/', top),
    url(r'^browse/', browse),
    url(r'^vote/(.*)$', vote),
    url(r'^detail/(.+)$', detail),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
