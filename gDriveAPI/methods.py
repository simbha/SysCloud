from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from oauth2client.django_orm import Storage
from django.http import HttpResponse, Http404
from fileboard.models import UserAccounts, CredentialsModel

'''
Created on 04-Jul-2013

@author: ss
'''

def gDriveURL(user_account):
    CLIENT_ID = '176109184245-kanck7mcvhs4nkp4ppdo9ksirrhvavbt.apps.googleusercontent.com'
    CLIENT_SECRET = '-ZpE9GVpFMyRRPr0gavptQrq'
    
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    url = flow.step1_get_authorize_url()
    
    return HttpResponse(url)

def gDriveCredentials(code, user_account):
    CLIENT_ID = '176109184245-kanck7mcvhs4nkp4ppdo9ksirrhvavbt.apps.googleusercontent.com'
    CLIENT_SECRET = '-ZpE9GVpFMyRRPr0gavptQrq'
    
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    try:
        credentials = flow.step2_exchange(code)
        storage = Storage(CredentialsModel, 'id', user_account, 'credentials')
        storage.put(credentials)
        return HttpResponse(True)
    except FlowExchangeError:
        return HttpResponse(False)
    
def exists(user_account):
    storage = Storage(CredentialsModel, 'id', user_account, 'credentials')
    credentials = storage.get()
    if credentials is not None:
        return HttpResponse(True)
    else:
        return HttpResponse(False)