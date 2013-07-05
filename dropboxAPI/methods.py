from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from fileboard.models import UserAccessToken, UserRequestToken, UserAccounts, Storage
from dropbox import client, session, rest
from dropbox.rest import ErrorResponse

'''
Created on 04-Jul-2013

@author: ss
'''

def dropboxURL(user_account):
    APP_KEY = 'zcw39nd2i33p78c'
    APP_SECRET = 'qnuut37muivao2v'
    ACCESS_TYPE = 'dropbox'
    
    sess = session.DropboxSession(APP_KEY,APP_SECRET,ACCESS_TYPE)
    request_token = sess.obtain_request_token()
    url = sess.build_authorize_url(request_token)
    request_token_key = request_token.key
    request_token_secret = request_token.secret
        
    try:
        user_request_token = UserRequestToken.objects.get(user_account=user_account)
        user_request_token.request_token_key = request_token_key
        user_request_token.request_token_secret = request_token_secret
        user_request_token.save()
    except UserRequestToken.DoesNotExist:
        user_request_token = UserRequestToken(user_account=user_account,request_token_key=request_token_key,request_token_secret=request_token_secret)
        user_request_token.save()
    
    return HttpResponse(url)

def dropboxAccessToken(user, account):  
    APP_KEY = 'zcw39nd2i33p78c'
    APP_SECRET = 'qnuut37muivao2v'
    ACCESS_TYPE = 'dropbox'
    
    
    storage_type = get_object_or_404(Storage, storage_type='dropbox')
    try:
        user_account = UserAccounts.objects.get(account=account,storage_type=storage_type,user=user)
        try:
            user_request_token = UserRequestToken.objects.get(user_account=user_account)
        except:
            return HttpResponse(False)
            
        sess = session.DropboxSession(APP_KEY,APP_SECRET,ACCESS_TYPE)
        request_token_key = user_request_token.get_request_token_key()
        request_token_secret = user_request_token.get_request_token_secret()
        sess.set_request_token(request_token_key, request_token_secret)
        try:
            access_token = sess.obtain_access_token()
            access_token_key = access_token.key
            access_token_secret = access_token.secret
            user_access_token = UserAccessToken(user_account=user_account,access_token_key=access_token_key,access_token_secret=access_token_secret)
            user_access_token.save()
            return HttpResponse(True)
        except ErrorResponse:
            return HttpResponse(False)
    except UserAccounts.DoesNotExist:
        raise Http404
