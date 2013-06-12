from django.db import models

# Create your models here.

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