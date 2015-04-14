from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^home/$', 'twitHits.userapp.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^userapp/', include('userapp.urls'),name='userapp'),
    url(r'^admin/', include(admin.site.urls)),
)
