from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_display = ('title', 'venue', 'starts_at', 'ends_at',)
    list_filter = ('created_at', 'updated_at', 'is_published')
    list_per_page = 50
    ordering = ('-created_at',)
    search_fields = ['title', ]