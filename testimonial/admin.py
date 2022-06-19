from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'updated_at',)
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = ('title',)
