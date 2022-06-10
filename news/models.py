from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField
from lib import forms, helpers, image

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    header_image = VersatileImageField('News Header', upload_to='images/news_headers/', ppoi_field='ppoi')
    ppoi = PPOIField('News Header PPOI')
    content = RichTextField()
    # excerpt = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'News'