from django.db import models
from django.dispatch import receiver
import ipdb

from .models import BoardMembers

from versatileimagefield.image_warmer import VersatileImageFieldWarmer

@receiver(models.signals.post_save, sender=BoardMembers)
def warm_Person_headshot_images(sender, instance, **kwargs):
    person_img_warmer = VersatileImageFieldWarmer(
        # ipdb.set_trace(),
        instance_or_queryset=instance,
        rendition_key_set=[
            ('squared', 'crop__200x200'),
        ],
        image_attr='image'
    )
    num_created, failed_to_create = person_img_warmer.warm()
    print('num_created')