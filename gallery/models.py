from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/images/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')