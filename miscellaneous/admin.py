from django.contrib import admin

from .models import Miscellaneous, MiscellaneousImage, Download


class MiscellaneousImageInline(admin.TabularInline):
    model = MiscellaneousImage
    extra = 1


@admin.register(Miscellaneous)
class MiscellaneousAdmin(admin.ModelAdmin):
    inlines = [MiscellaneousImageInline]
    list_display = ('title', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploaded_at',)
    date_hierarchy = 'uploaded_at'
    list_filter = ('uploaded_at',)
    list_per_page = 6
    ordering = ('-uploaded_at',)
    search_fields = ('title',)
