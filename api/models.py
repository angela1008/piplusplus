from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
## User Extension
class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    user_pic = models.ImageField(upload_to = 'static/media/user/', default = 'static/media/user/default.png')
    gender = models.CharField(max_length=20, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    self_introduction = models.TextField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


## Group's classification
class Classification(models.Model):
    name = models.CharField(max_length=254)
    
    def __unicode__(self):
      return self.name


## User's Interests
class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ManyToManyField(Classification, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    
## Group
class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    group_pic = models.ImageField(upload_to='static/media/group/', default='static/media/group/default.png')
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
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    is_leader = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
      return str(self.member)
    

## Event
class Event(models.Model):
    creater = models.ForeignKey(Membership, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default="")
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=100, null=True)
    join_number=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class EventShip(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_join = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


## Task
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254,blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default="")
    deadline_date = models.DateField(blank=True, null=True)
    deadline_time = models.TimeField(blank=True, null=True)
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
    creater = models.ForeignKey(Membership, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=254)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default="")
    heart_number = models.IntegerField(default=0)
    comment_number = models.IntegerField(default=0)
    share_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
class DiscussionHeart(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_heart = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class Comment(models.Model):
    creater = models.ForeignKey(Membership, on_delete=models.CASCADE)
    content = models.TextField(max_length=254)
    heart_number = models.IntegerField(default=0)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE,default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.content
        
class DiscussionComment(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class CommentHeart(models.Model):
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    is_heart = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class Note(models.Model):
    creater = models.ForeignKey(Membership, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default="")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __unicode__(self):
        return self.name