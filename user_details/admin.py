from django.contrib import admin
from django.contrib.auth.models import User

from user_details.models import Profile


class UserProfileInline(admin.StackedInline):
    """
    create class for profile inline view
    """
    model = Profile
    fk_name = 'user'


class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

