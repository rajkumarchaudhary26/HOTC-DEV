from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from ckeditor.fields import RichTextField


class Home(models.Model):
    content = RichTextField()
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name_plural = 'Home'