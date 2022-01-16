from django.conf import settings
from django.contrib import admin
from .models import *

site_name = settings.SITE_NAME.title()
admin.site.site_title = site_name
admin.site.site_header = f'{site_name} Admin'.title()
# admin.site.site_url = settings.SITE_URL


@admin.register(RandomUUID)
class RandomUUIDAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_on', 'updated_on')
    search_fields = ('uuid',)
    list_filter = ('created_on',)
    readonly_fields = ('uuid',)

