from django.db import models
from django.contrib.auth.models import User
from oauth2client.django_orm import CredentialsField

# Create your models here.

class Storage(models.Model):
    storage_type = models.CharField(max_length=100)
    
class UserAccounts(models.Model):
    account = models.CharField(max_length=100)
    storage_type = models.ForeignKey(Storage)
    user = models.ForeignKey(User) 

class UserRequestToken(models.Model):
    def get_request_token_key(self):
        return self.request_token_key
    def get_request_token_secret(self):
        return self.request_token_secret
    user_account = models.ForeignKey(UserAccounts)
    request_token_key = models.CharField(max_length=100)
    request_token_secret = models.CharField(max_length=100)

class UserAccessToken(models.Model):
    def get_access_token_key(self):
        return self.access_token_key
    def get_access_token_secret(self):
        return self.access_token_secret
    user_account = models.ForeignKey(UserAccounts)
    access_token_key = models.CharField(max_length=100)
    access_token_secret = models.CharField(max_length=100)
    
class CredentialsModel(models.Model):
    id = models.ForeignKey(UserAccounts, primary_key=True)
    credentials = CredentialsField()

class File(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_dir = models.BooleanField()
    mime_type = models.CharField(max_length=50,default=None)
    last_modified = models.DateTimeField()
    modified_by = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    root = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    owned_by = models.CharField(max_length=100)