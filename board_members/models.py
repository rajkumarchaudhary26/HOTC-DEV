from hashlib import blake2b
from re import T
from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField


class BoardMembers(models.Model):
    name = models.CharField(max_length=50)
    image = VersatileImageField(
        upload_to='images/board_members/', null=True, blank=True, ppoi_field='ppoi')
    ppoi = PPOIField()
    designation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Board Members'

    def get_absolute_url(self):
        return 'board-member/{}'.format(self.name)
    
