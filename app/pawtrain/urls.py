
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

from web import urls

urlpatterns = patterns('',

    url(r'^accounts/', include('allauth.urls')),

    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='account_login'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='account_signup'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^', include(urls)),
)
