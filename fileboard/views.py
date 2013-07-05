from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from fileboard.models import UserAccessToken, UserRequestToken, UserAccounts, Storage
import dropboxAPI.methods
import gDriveAPI.methods

# Create your views here.
    
def addUserAccount(account, storage_type, user):
    try:
        user_account = UserAccounts.objects.get(account=account,storage_type=storage_type,user=user)
    except UserAccounts.DoesNotExist:
        user_account = UserAccounts(account=account,storage_type=storage_type,user=user)
        user_account.save()
        
    return user_account

def getGDriveURL(request):
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='google-drive')
        account = request.POST.get('account')
        user_account = addUserAccount(account, storage_type, user)
        return gDriveAPI.methods.gDriveURL(user_account)
    else:
        raise Http404
    
def getGDriveCredentials(request):
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='google-drive')
        account = request.POST.get('account')
        user_account = addUserAccount(account, storage_type, user)
        code = request.POST.get('code')
        return gDriveAPI.methods.gDriveCredentials(code, user_account)
    else:
        raise Http404
    
def getDropboxURL(request):
    c = {}
    c.update(csrf(request))
    
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='dropbox')
        account = request.POST.get('account')
        user_account = addUserAccount(account, storage_type, user)
        return dropboxAPI.methods.dropboxURL(user_account)
    else:
        raise Http404

def getDropboxAccessToken(request):  
    c = {}
    c.update(csrf(request))
    
    if request.user.is_authenticated():
        account = request.POST.get('account')
        return dropboxAPI.methods.dropboxAccessToken(request.user, account)
    else:
        raise Http404
    
def newAccount(request, account_type):
    return render(request, 'fileboard/accounts/new-' + account_type + '.html')

def manageAccount(request, account_type):
    return render(request, 'fileboard/accounts/manage-' + account_type + '.html')

def exists(request):
    if request.user.is_authenticated():
        user = request.user
        account = request.POST.get('account') 
        storage_type = get_object_or_404(Storage, storage_type=request.POST.get('storageType'))
        try:
            user_account = UserAccounts.objects.get(account=account,storage_type=storage_type,user=user)
            if storage_type.storage_type == 'dropbox':
                try: 
                    user_access_token = UserAccessToken.objects.get(user_account=user_account)
                    return HttpResponse(True)
                except UserAccessToken.DoesNotExist:
                    return HttpResponse(False)
            elif storage_type.storage_type == 'google-drive':
                return gDriveAPI.methods.exists(user_account)
        except UserAccounts.DoesNotExist:
            return HttpResponse(False)               
        
def accounts(request):
    if request.user.is_authenticated():
        return render(request, 'fileboard/accounts.html')
    else:
        raise Http404
    
def permission(request):
    c = {}
    c.update(csrf(request))
    
    if request.user.is_authenticated():
        user_accounts = UserAccounts.objects.filter(user=request.user)
        if len(user_accounts) > 0:
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        raise Http404

def index(request):
    if request.user.is_authenticated():
        user_accounts = UserAccounts.objects.filter(user=request.user)
        if len(user_accounts) > 0:
            return HttpResponse(True)
        #return getUserFileboard(request, user)
    else:
        raise Http404

