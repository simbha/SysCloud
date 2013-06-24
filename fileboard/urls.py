from django.conf.urls import patterns, url

from fileboard import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<email_id>[A-za-z0-9@.]+)/(?P<session_key>[A-za-z0-9]+)/$', views.index, name='index'),
)
