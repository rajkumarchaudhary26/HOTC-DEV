from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext as _

ENABLED_MODELS = ['miscellaneous', 'about', 'gallery']


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.SlugField(unique=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.PROTECT, related_name='menu_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ENABLED_MODELS},
                                     blank=True, null=True,
                                     help_text=_('Please select the type of the menu item, e.g. about or gallery.'))
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    link = models.CharField(max_length=255, blank=True)
    enabled = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.object_id:
            if not self.title:
                self.title = str(self.content_object)
                print(self.title)
            if not self.link:
                self.link = self.content_object.get_absolute_url()
            super().save(*args, **kwargs)
        else:
            pass

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
