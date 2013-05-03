from django.contrib import admin

from .models import Release


class ReleaseAdmin(admin.ModelAdmin):
    ordering = ['-created']

admin.site.register(Release, ReleaseAdmin)
