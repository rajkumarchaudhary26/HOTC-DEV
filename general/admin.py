from django.contrib import admin

from .models import BoardMembers, OrganizationStructure, Contact, Testimonial


@admin.register(BoardMembers)
class BoardMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at', 'updated_at',)


@admin.register(OrganizationStructure)
class OrganizationStructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)


@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'updated_at',)
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = ('title',)
