from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=255)
    image = VersatileImageField(
        upload_to='images/about/', ppoi_field='ppoi', null=True, blank=True)
    ppoi = PPOIField('About Image PPOI')
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'about'
