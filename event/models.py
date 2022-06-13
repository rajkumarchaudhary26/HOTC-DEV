from django.db import models
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField, PPOIField

from lib.helpers import get_excerpt


class Event(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = VersatileImageField(blank=True, null=True, upload_to='images/event/', ppoi_field='ppoi')
    ppoi = PPOIField('Event Images PPOI')
    content = RichTextField()
    excerpt = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower().replace('  ', ' ').replace(' ', '-').replace('_', '-')
        if not self.excerpt:
            self.excerpt = get_excerpt(self.content)
        super().save(*args, **kwargs)