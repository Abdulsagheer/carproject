from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:10px;"/>'.format(object.photo.url))
    thumbnail.short_description='Photo'
    search_fields=('id','first_name','last_name','designation')

    list_display=('id','thumbnail','first_name','last_name','designation','created_date')
    list_display_links=('id','first_name','last_name')
    list_filter=('id','designation','created_date')

   
   
    



admin.site.register(Team,TeamAdmin)

