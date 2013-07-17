from django.http import HttpResponse
from fileboard.models import UserAccounts, UserAccessToken
from skydrive import api_v5, conf
import os
from skydrive.api_v5 import AuthenticationError

'''
Created on 12-Jul-2013

@author: ss
'''
 
def skydriveURL(user_account): 
    fo = open("/home/ss/user-account-%s" % user_account.pk, "a")
    fo.write( "client:\r\n  id: 00000000440FC402\r\n  secret: dH-qDE2M0o9phschaLwvSKDGWyFTYS7z");
    fo.close()
    api = api_v5.PersistentSkyDriveAPI.from_conf("/home/ss/user-account-%s" % user_account.pk)  
    url = format(api.auth_user_get_url())
    return HttpResponse(url)

def skydriveAccessToken(url,user_account):
    try:
        api = api_v5.PersistentSkyDriveAPI.from_conf("/home/ss/user-account-%s" % user_account.pk) 
        api.auth_user_process_url(url)
        api.auth_get_token()
        user_account.access = True
        user_account.save()
        return HttpResponse(True)
    except AuthenticationError:
        return HttpResponse(False)