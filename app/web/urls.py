
# -*- coding: utf-8 -*-
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# PAWTRAIN
#
#     Pet underground railroad
#
#
# Authors: Baron L. Chandler, baron@venturecranial.com
# -----------------------------------------------------------------------
# COPYRIGHT ©2014 Venture Cranial, LLC
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#

from django.conf.urls import patterns, include, url
from web.views import (
    account_profile, dashboard, index, transport_detail,)

urlpatterns = patterns('',
    url(r'^$', 'web.views.index', name='pawtrain_index'),
    url(r'^dashboard/$', 'web.views.dashboard', name='pawtrain_dashboard'),

    url(r'^accounts/profile/$', 'web.views.account_profile', name='pawtrain_profile'),

    url(r'^transport/(?P<tracking_number>PT\w+)$', 'web.views.transport_detail', name='transport_detail'),

)
