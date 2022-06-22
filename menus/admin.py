from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(SortableInlineAdminMixin, admin.StackedInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('name', 'code', 'enabled')
    prepopulated_fields = {'code': ('name',)}
    list_filter = ('enabled',)
    search_fields = ('name', 'code')
    inlines = (MenuItemInline,)


@admin.register(MenuItem)
class MenuItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'link', 'enabled')
    list_filter = ('menu', 'enabled', 'content_type', 'updated_at')
    search_fields = ('title', 'link')