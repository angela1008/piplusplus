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


## Activity
class Activity(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=254, blank=True)
	time = models.DateField(blank=True, null=True)
	location = models.CharField(max_length=100)
	join_number=models.IntegerField(default=0)##
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
	    return self.title


class ActivityShip(models.Model):
	 member = models.ForeignKey(User, on_delete=models.CASCADE)
	 activity=models.ForeignKey(Activity, on_delete=models.CASCADE)
	 club = models.ForeignKey(Club, on_delete=models.CASCADE)
	 is_leader = models.BooleanField(default=False)


## Progress
class Progess(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=254,blank=True)
	time=models.DateField(max_length=100)
	join_number=models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True) 
	
	def __unicode__(self):
	    return self.title


class ProgessShip(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    progess = models.ForeignKey(Progess, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
