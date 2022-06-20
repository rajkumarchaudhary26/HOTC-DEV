from django.contrib import admin

from .models import BoardMembers


@admin.register(BoardMembers)
class BoardMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at', 'updated_at',)
