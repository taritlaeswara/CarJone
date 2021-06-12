from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from pages.models import Team

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style ="border-radius:50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'photo'
    list_display = ('id','thumbnail','first_name', 'designation','created_table')
    list_display_links = ('id','first_name','thumbnail', )
    search_fields = ('first_name','last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)