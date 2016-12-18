from django.contrib import admin
from api import models as apiModels

# Register your models here.
class UserExtensionAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'birth', 'interest', 'lacation', 'self_introduction', 'created_at', 'updated_at')

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'club', 'date_joined', 'is_leader')

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'club_introduction', 'created_at', 'updated_at')

admin.site.register(apiModels.UserExtension, UserExtensionAdmin)
admin.site.register(apiModels.Membership, MembershipAdmin)
admin.site.register(apiModels.Club, ClubAdmin)