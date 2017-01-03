from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
## User Extension
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    self_introduction = models.TextField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


## User's Interests
class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


## Group's classification
class Classification(models.Model):
    name = models.CharField(max_length=254)
    
    def __unicode__(self):
      return self.name
    
## Group
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    group_introduction = models.TextField(max_length=254, blank=True, null=True)
    join_number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    ## Return group name instead of "Group Object"
    def __unicode__(self):
      return self.name
      
    
class Membership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
      return str(self.member)
    

## Event
class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    join_number=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class EventShip(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


## Task
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254,blank=True, null=True)
    deadline = models.DateField()
    finished_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class TaskShip(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    
## Discussion
class Discussion(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254)
    heart_number = models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    share_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
class DiscussionShip(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_heart = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=False)
    is_share = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class Comment(models.Model):
    content = models.TextField(max_length=254)
    heart_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.content

class CommentShip(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    is_heart = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)