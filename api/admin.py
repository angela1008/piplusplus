from django.contrib import admin
from api import models as apiModels

# Register your models here.
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'birth', 'location', 'self_introduction', 'created_at', 'updated_at')
    
class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'created_at', 'updated_at')
    

class ClassificationAdmin(admin.ModelAdmin):
    ist_display = ('id', 'name')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'leader', 'classification', 'group_introduction', 'join_number', 'created_at', 'updated_at')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'group', 'date_joined', 'is_leader', 'created_at', 'updated_at')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'time', 'location', 'join_number', 'created_at', 'updated_at')

class EventShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'event', 'group', 'is_leader', 'created_at', 'updated_at')
	
	
class TaskAdmin(admin.ModelAdmin):
	 list_display = ('id', 'title', 'content', 'deadline', 'finished_number', 'created_at', 'updated_at')
	 
class TaskShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'task', 'group', 'is_finished', 'created_at', 'updated_at')
	
	
class DiscussionAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'content', 'heart_number', 'comment_number', 'share_number', 'created_at', 'updated_at')

class DiscussionShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'discussion', 'group', 'is_heart', 'is_comment', 'is_share', 'created_at', 'updated_at')
	
	
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'heart_number', 'created_at', 'updated_at')
    
class CommentShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'comment', 'discussion', 'is_heart', 'created_at', 'updated_at')
    
    
admin.site.register(apiModels.UserExtension, UserExtensionAdmin)
admin.site.register(apiModels.UserInterest, UserInterestAdmin)

admin.site.register(apiModels.Classification, ClassificationAdmin)
admin.site.register(apiModels.Group, GroupAdmin)
admin.site.register(apiModels.Membership, MembershipAdmin)

admin.site.register(apiModels.Event, EventAdmin)
admin.site.register(apiModels.EventShip, EventShipAdmin)

admin.site.register(apiModels.Task, TaskAdmin)
admin.site.register(apiModels.TaskShip, TaskShipAdmin)

admin.site.register(apiModels.Discussion, DiscussionAdmin)
admin.site.register(apiModels.DiscussionShip, DiscussionShipAdmin)

admin.site.register(apiModels.Comment, CommentAdmin)
admin.site.register(apiModels.CommentShip, CommentShipAdmin)