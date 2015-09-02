from django.contrib import admin
from session.models import Speaker


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
