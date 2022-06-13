from versatileimagefield.fields import VersatileImageField, PPOIField

from django.db import models

# Model that holds record for Transplant acts and legislations
class Miscellaneous(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Miscellaneous'

class MiscellaneousImage(models.Model):
    image = VersatileImageField(upload_to='images/miscellaneous/', ppoi_field='ppoi')
    ppoi = PPOIField('Miscellaneous Images PPOI')
    miscellaneous = models.ForeignKey(Miscellaneous, on_delete=models.CASCADE, related_name='images')