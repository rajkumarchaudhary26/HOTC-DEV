from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField

from lib.helpers import get_excerpt

class News(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    header_image = VersatileImageField('News Header', upload_to='images/news_headers/', ppoi_field='ppoi')
    ppoi = PPOIField('News Header PPOI')
    content = RichTextField()
    excerpt = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower().replace('  ', ' ').replace(' ', '-').replace('_', '-')
        if not self.excerpt:
            self.excerpt = get_excerpt(self.content)
        super().save(*args, **kwargs)