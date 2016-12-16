from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
## User
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True, null=True)
    birth = models.CharField(max_length=50, blank=True, null=True)#
    lacation = models.CharField(max_length=100, blank=True, null=True)
    self_introduction = models.CharField(max_length=300, blank=True, null=True)#
    interest = models.CharField(max_length=300, blank=True, null=True)#
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)