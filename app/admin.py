from django.contrib import admin
from .models import UserProfile,Event,UserToken,Registration,EventRules,RegistrationManagement,TeamLeader,RatingModel,UserRated
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):

    list_display=('event','team_name','admission','token')

    def get_queryset(self,request):
        queryset=super(RegistrationAdmin,self).get_queryset(request)
        queryset=queryset.order_by('event','team_name','admission')
        return queryset

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','branch','name','coins','phone','admission')

    def get_queryset(self,request):
        queryset=super(UserProfileAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-coins','-user','-branch','-phone')
        return queryset

class EventAdmin(admin.ModelAdmin):
    list_display=('name',)

class TeamLeaderAdmin(admin.ModelAdmin):
    list_display=('event','team_name','adm_no','phone',)

class RegistrationManagementAdmin(admin.ModelAdmin):
    list_display=('team_name','current_event',)

class RatingModelAdmin(admin.ModelAdmin):
    list_display=('event','average_rating','number_of_rates')

class UserRatedAdmin(admin.ModelAdmin):
    list_display=('user')

class UserTokenAdmin(admin.ModelAdmin):

    list_display=('user.userprofile.admission',)

    def get_queryset(self,request):
        queryset=super(UserTokenAdmin,self).get_queryset(request)
        queryset=queryset.order_by('user.userprofile.admission',)
        return queryset

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(UserToken)
admin.site.register(EventRules)
admin.site.register(RegistrationManagement,RegistrationManagementAdmin)
admin.site.register(TeamLeader,TeamLeaderAdmin)
admin.site.register(RatingModel,RatingModelAdmin)
admin.site.register(UserRated)
admin.site.site_header='Admin'