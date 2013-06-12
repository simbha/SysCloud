from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^authorise/$', views.authorise, name='authorise'),
)
