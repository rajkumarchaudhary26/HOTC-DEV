from django.contrib import admin

from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}