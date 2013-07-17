from django.http import HttpResponse
from fileboard.models import UserAccounts, UserAccessToken
from dropbox.client import DropboxOAuth2FlowNoRedirect, DropboxClient
from dropbox import rest as dbrest
from fileboard.file_struct import File
'''
Created on 04-Jul-2013

@author: ss
'''

def getImage(mime_type):
    if mime_type == 'text/plain':
        return 'fileboard/images/file.png'
    elif mime_type == 'application/pdf':
        return 'fileboard/images/pdf.png'
    elif mime_type == 'application/x-tar':
        return 'fileboard/images/tar.png'
    elif mime_type == 'application/zip':
        return 'fileboard/images/zip.png'
    elif mime_type.startswith('image'):
        return 'fileboard/images/picture.png'
    
    
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
        user_access_token = UserAccessToken(user_account=user_account,access_token=access_token)
        user_access_token.save()
        user_account.access = True
        user_account.save()
        return HttpResponse(True)
    except dbrest.ErrorResponse:
        return HttpResponse(False)
    
def dropboxFileTree(root, user_account):
    try:
        user_access_token = UserAccessToken.objects.get(user_account=user_account)
        access_token = user_access_token.access_token
        client = DropboxClient(access_token)
        folder_metadata = client.metadata(root)
        folder_contents = folder_metadata.get('contents')
        file_list = []
        for content in folder_contents:
            name = content.get('path')
            isDir = content.get('is_dir')
            if isDir is True:
                image = 'fileboard/images/folder1.png'
            else:
                mime_type = content.get('mime_type')
                image = getImage(mime_type)
            this_file = File('dropbox',name,image)
            file_list.append(this_file)
        return file_list 
    except UserAccessToken.DoesNotExist:
        return None
