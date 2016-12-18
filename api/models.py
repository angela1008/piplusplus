from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
## User
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    lacation = models.CharField(max_length=50, blank=True, null=True)
    self_introduction = models.TextField(max_length=254, blank=True, null=True)
    interest = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    
## Club
class Club(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    club_introduction = models.TextField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    ## Return club name instead of "Club Object"
    def __unicode__(self):
      return self.name
    
    
class Membership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_leader = models.BooleanField(default=False)
