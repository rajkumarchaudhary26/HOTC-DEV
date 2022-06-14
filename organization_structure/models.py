from contextlib import nullcontext
from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField

class OrganizationStructure(models.Model):
    title = models.CharField(max_length=255)
    image = VersatileImageField(upload_to='images/organization_structure/', null=True, blank=True, ppoi_field='ppoi')
    ppoi = PPOIField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Organization Structure'