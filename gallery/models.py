from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'

class Image(models.Model):
    image = models.ImageField(upload_to='images/images/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')