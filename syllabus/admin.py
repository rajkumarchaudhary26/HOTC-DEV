from django.contrib import admin

from .models import Syllabus


@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}
