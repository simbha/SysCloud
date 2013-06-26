from django.db import models
from login.models import RegisteredUsers

# Create your models here.

class UserAccessToken(models.Model):
    def get_access_token(self):
        return self.access_token
    user = models.ForeignKey(RegisteredUsers)
    access_token = models.CharField(max_length=100)

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