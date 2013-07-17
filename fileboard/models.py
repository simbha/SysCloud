from django.db import models
from django.contrib.auth.models import User
from oauth2client.django_orm import CredentialsField

# Create your models here.

class Storage(models.Model):
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
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