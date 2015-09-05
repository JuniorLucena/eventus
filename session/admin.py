from django.contrib import admin
from session.models import Speaker, EntrySession


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

@admin.register(EntrySession)
class EntrySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'status')
