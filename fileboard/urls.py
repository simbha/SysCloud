from django.conf.urls import patterns, url

from fileboard import views
urlpatterns = patterns('',
    url(r'^$', views.getUserFileboard, name='index'),
    url(r'^permissions$', views.permission, name='permission'),
    url(r'^accounts$', views.accounts, name='accounts'),
    url(r'^accounts/exists$', views.exists, name='accountExists'),
    url(r'^accounts/(?P<account_type>[a-z\-]+)/create$', views.newAccount, name='newAccount'),
    url(r'^accounts/(?P<account_type>[a-z\-]+)/manage$', views.manageAccount, name='manageAccount'),
    url(r'^accounts/(?P<account_type>[a-z\-]+)/delete$', views.deleteAccount, name='deleteAccount'),
    url(r'^getURL/google-drive$', views.getGDriveURL, name='gDriveURL'),
    url(r'^getAccess/google-drive$', views.getGDriveCredentials, name='gDriveCredentials'),
    url(r'^getURL/dropbox$', views.getDropboxURL, name='dropboxURL'),
    url(r'^getAccess/dropbox$', views.getDropboxAccessToken, name='dropboxAccessToken'),
    url(r'^removeAccess/dropbox$', views.destroyDropboxAccessToken, name='destroyAccessToken'),
    url(r'^getURL/skydrive$', views.getSkyDriveURL, name='skydriveURL'),
    url(r'^getAccess/skydrive$', views.getSkyDriveAccessToken, name='skydriveAccessToken'),
    url(r'^removeAccess/skydrive$', views.destroySkyDriveAccessToken, name='destroyAccessToken'),
    url(r'^files$', views.getUserFiles, name='userFileboard')
)
