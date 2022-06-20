from versatileimagefield.fields import VersatileImageField, PPOIField

from django.db import models

from home.models import Home


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    featured_image = VersatileImageField(
        upload_to='images/gallery/featured/', ppoi_field='ppoi')
    ppoi = PPOIField('Featured Images PPOI')
    home = models.ForeignKey(
        Home, on_delete=models.PROTECT, related_name='gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'


class Image(models.Model):
    image = VersatileImageField(upload_to='images/gallery/', ppoi_field='ppoi')
    ppoi = PPOIField('Gallery PPOI')
    gallery = models.ForeignKey(
        Gallery, on_delete=models.PROTECT, related_name='images')
