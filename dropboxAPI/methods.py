from django.http import HttpResponse
from fileboard.models import UserAccounts, UserAccessToken
from dropbox.client import DropboxOAuth2FlowNoRedirect
from dropbox import rest as dbrest
'''
Created on 04-Jul-2013

@author: ss
'''

def dropboxURL(user_account):
    APP_KEY = 'zcw39nd2i33p78c'
    APP_SECRET = 'qnuut37muivao2v'
    
    oauth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    url = oauth_flow.start()
    
    return HttpResponse(url)

def dropboxAccessToken(code, user_account):  
    APP_KEY = 'zcw39nd2i33p78c'
    APP_SECRET = 'qnuut37muivao2v'
    
    oauth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
    
    try:
        access_token, user_id = oauth_flow.finish(code)
        print access_token
        user_access_token = UserAccessToken(user_account=user_account,access_token=access_token)
        user_access_token.save()
        user_account.access = True
        user_account.save()
        return HttpResponse(True)
    except dbrest.ErrorResponse:
        return HttpResponse(False)
