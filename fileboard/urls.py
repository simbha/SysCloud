from django.conf.urls import patterns, url

from fileboard import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^permissions$', views.permission, name='permission'),
    url(r'^accounts$', views.accounts, name='accounts'),
    url(r'^accounts/exists$', views.exists, name='accountExists'),
    url(r'^accounts/(?P<account_type>[a-z\-]+)/create$', views.newAccount, name='newAccount'),
    url(r'^accounts/(?P<account_type>[a-z\-]+)/manage$', views.manageAccount, name='manageAccount'),
    url(r'^getURL/google-drive$', views.getGDriveURL, name='gDriveURL'),
    url(r'^getAccess/google-drive$', views.getGDriveCredentials, name='gDriveCredentials'),
    url(r'^getURL/dropbox$', views.getDropboxURL, name='dropboxURL'),
    url(r'^getAccess/dropbox$', views.getDropboxAccessToken, name='dropboxAccessToken')
)
