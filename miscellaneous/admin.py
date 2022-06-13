from django.contrib import admin

from .models import Miscellaneous, MiscellaneousImage

class MiscellaneousImageInline(admin.TabularInline):
    model = MiscellaneousImage
    extra = 1

@admin.register(Miscellaneous)
class MiscellaneousAdmin(admin.ModelAdmin):
    inlines = [MiscellaneousImageInline]
    list_display = ('title', 'created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('title',)}