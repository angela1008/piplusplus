from django.contrib import admin
from api import models as apiModels

# Register your models here.
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birth', 'interest', 'location', 'self_introduction', 'created_at', 'updated_at')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'club', 'date_joined', 'is_leader', 'created_at', 'updated_at')

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'club_introduction', 'created_at', 'updated_at')
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time', 'location', 'join_number', 'created_at', 'updated_at')

class EventShipAdmin(admin.ModelAdmin):
	list_display = ('member', 'event', 'club', 'created_at', 'updated_at')
	
class ProgressAdmin(admin.ModelAdmin):
	 list_display = ('title', 'content', 'deadline', 'finished_number', 'created_at', 'updated_at')
	 
class ProgressShipAdmin(admin.ModelAdmin):
	list_display = ('member', 'progress', 'club', 'is_finished', 'created_at', 'updated_at')
    
    
admin.site.register(apiModels.UserExtension, UserExtensionAdmin)
admin.site.register(apiModels.Membership, MembershipAdmin)
admin.site.register(apiModels.Club, ClubAdmin)
admin.site.register(apiModels.Event, EventAdmin)
admin.site.register(apiModels.EventShip, EventShipAdmin)
admin.site.register(apiModels.Progress, ProgressAdmin)
admin.site.register(apiModels.ProgressShip, ProgressShipAdmin)