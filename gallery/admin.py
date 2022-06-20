from django.contrib import admin

from .models import Image, Gallery


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)