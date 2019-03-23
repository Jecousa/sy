from django.contrib import admin

from .models import Service, PlayMusic, SearchMusic

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'description')
    list_display_links = ('id', 'title')
admin.site.register(Service, ServiceAdmin)
admin.site.register(PlayMusic)
admin.site.register(SearchMusic)