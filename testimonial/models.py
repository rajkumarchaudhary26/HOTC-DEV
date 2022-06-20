from django.db import models

from versatileimagefield.fields import VersatileImageField
from ckeditor.fields import RichTextField


class Testimonial(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image = VersatileImageField(
        upload_to='images/testimonial/', null=True, blank=True)
    description = RichTextField()
    created_at = models.DateTimeField(
        auto_now_add=True, editable=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title
