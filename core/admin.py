from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from core.models import UserProfile

admin.site.unregister(get_user_model())


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 1


@admin.register(get_user_model())
class UserAdmin(AuthUserAdmin):
    inlines = [
        UserProfileInline,
    ]
