from django.conf.urls import patterns, url

from userapp import views

urlpatterns = patterns('',url(r'^$', views.index, name='index'), url(r'home/$',views.home,name='home'),)