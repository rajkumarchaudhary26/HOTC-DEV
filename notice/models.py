from django.db import models

from lib.helpers import get_excerpt

from ckeditor.fields import RichTextField


class Notice(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    content = RichTextField()
    excerpt = models.TextField(blank=True)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower().replace(
            '  ', ' ').replace(' ', '-').replace('_', '-')
        if not self.excerpt:
            self.excerpt = get_excerpt(self.content)
        super().save(*args, **kwargs)
