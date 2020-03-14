from django.contrib import admin
from webapp.models import FileBase


class FileBaseTab(admin.ModelAdmin):
    model = FileBase
    readonly_fields = ['creation_date', 'numder_of_downloads']
    exclude = []


admin.site.register(FileBase, FileBaseTab)