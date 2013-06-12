from django.db import models

# Create your models here.
    
class RegisteredUsers(models.Model):
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    email = models.EmailField()
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, default=None)