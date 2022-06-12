from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['slug','title', 'created_at', 'updated_at', 'is_published']
    prepopulated_fields = {'slug': ('title',)}