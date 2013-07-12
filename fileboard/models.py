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
    access = models.BooleanField()

class UserAccessToken(models.Model):
    user_account = models.ForeignKey(UserAccounts)
    access_token = models.CharField(max_length=100)
    
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