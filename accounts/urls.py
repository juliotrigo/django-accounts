from django.conf.urls import patterns, url

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'accounts/login.xhtml'}, name='login'),
    url(r'^logout/$', 'logout', {'template_name': 'accounts/logout.xhtml'}, name='logout'),
)

urlpatterns += patterns('',
    url(r'^profile/$', 'profile', name='profile', prefix='accounts.views'),
)