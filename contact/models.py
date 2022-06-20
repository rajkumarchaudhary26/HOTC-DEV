from django.db import models

from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = RichTextField()

    def __str__(self):
        return self.name
