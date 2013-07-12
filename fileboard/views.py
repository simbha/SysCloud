from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from fileboard.models import UserAccessToken, UserAccounts, Storage, CredentialsModel
import dropboxAPI.methods
import gDriveAPI.methods

# Create your views here.
    
def addUserAccount(account, storage_type, user, access):
    try:
        user_account = UserAccounts.objects.get(account=account,storage_type=storage_type,user=user,access=access)
    except UserAccounts.DoesNotExist:
        user_account = UserAccounts(account=account,storage_type=storage_type,user=user,access=access)
        user_account.save()
        
    return user_account

def getGDriveURL(request):
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='google-drive')
        account = request.POST.get('account')
        access = False
        user_account = addUserAccount(account, storage_type, user, access)
        return gDriveAPI.methods.gDriveURL(user_account)
    else:
        raise Http404
    
def getGDriveCredentials(request):
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='google-drive')
        account = request.POST.get('account')
        user_account = UserAccounts.objects.get(user=user,storage_type=storage_type,account=account)
        code = request.POST.get('code')
        return gDriveAPI.methods.gDriveCredentials(code, user_account)
    else:
        raise Http404
    
def getDropboxURL(request):
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='dropbox')
        account = request.POST.get('account')
        access = False
        user_account = addUserAccount(account, storage_type, user, access)
        return dropboxAPI.methods.dropboxURL(user_account)
    else:
        raise Http404

def getDropboxAccessToken(request):  
    if request.user.is_authenticated():
        user = request.user
        storage_type = get_object_or_404(Storage, storage_type='dropbox')
        account = request.POST.get('account')
        user_account = UserAccounts.objects.get(user=user,storage_type=storage_type,account=account)
        code = request.POST.get('code')
        return dropboxAPI.methods.dropboxAccessToken(code, user_account)
    else:
        raise Http404
    
def destroyDropboxAccessToken(request):
    if request.user.is_authenticated():
        account_id = request.POST.get('id')
        user_account = UserAccounts.objects.get(pk=account_id)
        user_access_token = UserAccessToken.objects.get(user_account=user_account)
        user_access_token.delete()
        user_account.access = False
        user_account.save()
        return HttpResponse(True)
    else:
        raise Http404
    
def newAccount(request, account_type):
    return render(request, 'fileboard/accounts/new-' + account_type + '.html')

def manageAccount(request, account_type):
    storage_type = Storage.objects.get(storage_type=account_type)
    user_account_list = UserAccounts.objects.filter(storage_type=storage_type,user=request.user)
    context = {'user_account_list': user_account_list}
    return render(request, 'fileboard/accounts/manage-' + account_type + '.html', context)

def deleteAccount(request, account_type):
    if request.user.is_authenticated():
        id = request.POST.get('id')
        try:
            user_account = UserAccounts.objects.get(pk=id)
            if account_type == 'dropbox':
                if user_account.access is True:
                    user_access_token = UserAccessToken.objects.get(user_account=user_account)
                    user_access_token.delete()
                user_account.delete()
            elif account_type == 'google-drive':
                if user_account.access is True:
                    credentials = CredentialsModel.objects.get(id=user_account)
                    credentials.delete()
            return HttpResponse(True)
        except UserAccounts.DoesNotExist:
            raise Http404

def exists(request):
    if request.user.is_authenticated():
        user = request.user
        account = request.POST.get('account') 
        storage_type = get_object_or_404(Storage, storage_type=request.POST.get('storageType'))
        try:
            user_account = UserAccounts.objects.get(account=account,storage_type=storage_type,user=user,access=True)
            return HttpResponse(True)
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
            return HttpResponse(False)
        else:
            return HttpResponse(False)
    else:
        raise Http404
    
def getUserFileboard(request, user):
    return render(request, 'fileboard/index.html')

def index(request):
    if request.user.is_authenticated():
        return getUserFileboard(request, request.user)
    else:
        raise Http404

