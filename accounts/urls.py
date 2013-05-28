# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

#urlpatterns = patterns('django.contrib.auth.views',
#    url(r'^login/$', 'login', {'template_name': 'accounts/login.html'}, name='login'),
#    url(r'^logout/$', 'logout', {'template_name': 'accounts/logout.html'}, name='logout'),
#)
#Using Custom wrappers
urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'custom_login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', 'custom_logout', {'template_name': 'accounts/logout.html'}, name='logout'),
)

urlpatterns += patterns('',
    url(r'^profile/$', 'profile', name='profile', prefix='accounts.views'),
)