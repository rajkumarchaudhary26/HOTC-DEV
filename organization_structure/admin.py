from django.contrib import admin

from .models import OrganizationStructure


@admin.register(OrganizationStructure)
class OrganizationStructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
