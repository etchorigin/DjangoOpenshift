from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^accounts/', include('accounts.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^profile/', 'openshift.views.profile', name='profile'),
	url(r'^accounts/', 'openshift.views.accounthome', name='accounthome'),
	url(r'^$', 'openshift.views.home', name='home'),
	
)
