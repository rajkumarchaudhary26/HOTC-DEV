from django.contrib import admin

from .models import Page, Home


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('content', 'uploaded_at', 'updated_at',)
