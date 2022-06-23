from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    image = VersatileImageField(
        upload_to='images/about/', ppoi_field='ppoi', null=True, blank=True)
    ppoi = PPOIField('About Image PPOI')
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 'about/{}'.format(self.slug)
