
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from web.views import index

urlpatterns = patterns('',
    url(r'^$', 'web.views.index', name='pawtrain_index'),
)
