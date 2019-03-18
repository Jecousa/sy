from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'description')
    list_display_links = ('id', 'title')
admin.site.register(Event, EventAdmin)