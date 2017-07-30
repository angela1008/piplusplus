from django.contrib import admin
from api import models as apiModels

# Register your models here.
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_pic', 'gender', 'birth', 'location', 'self_introduction', 'created_at', 'updated_at')


#class UserInterestInline(admin.TabularInline):
    #model = apiModels.UserInterest

class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')
    #inlines = (UserInterestInline,)
    #fields = ['name']
    

class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group_pic', 'leader', 'classification', 'group_introduction', 'join_number', 'created_at', 'updated_at')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'group', 'classification', 'date_joined', 'is_leader', 'created_at', 'updated_at')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'creater', 'title', 'group', 'content', 'start_date','start_time' ,'end_date','end_time' ,'location', 'join_number', 'created_at', 'updated_at')

class EventShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'event', 'group', 'is_join', 'created_at', 'updated_at')
	
	
class TaskAdmin(admin.ModelAdmin):
	 list_display = ('id', 'title', 'group' , 'content', 'deadline_date','deadline_time', 'finished_number', 'created_at', 'updated_at')
	 
class TaskShipAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'task', 'group', 'is_finished', 'created_at', 'updated_at')
	
	
class DiscussionAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'group', 'content', 'heart_number', 'comment_number', 'share_number', 'created_at', 'updated_at')

class DiscussionHeartAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'discussion', 'group', 'is_heart', 'created_at', 'updated_at')
	
class DiscussionCommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'member', 'comment', 'discussion', 'created_at', 'updated_at')
	
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'creater', 'content', 'discussion', 'heart_number', 'created_at', 'updated_at')
    
class CommentHeartAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'comment', 'discussion', 'is_heart', 'created_at', 'updated_at')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'creater', 'name', 'group', 'created_at', 'updated_at')
    
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
admin.site.register(apiModels.DiscussionHeart, DiscussionHeartAdmin)
admin.site.register(apiModels.DiscussionComment, DiscussionCommentAdmin)

admin.site.register(apiModels.Comment, CommentAdmin)
admin.site.register(apiModels.CommentHeart, CommentHeartAdmin)

admin.site.register(apiModels.Note, NoteAdmin)