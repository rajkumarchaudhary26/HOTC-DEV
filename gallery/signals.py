from django.db import models
from django.dispatch import receiver

from .models import Image

from versatileimagefield.image_warmer import VersatileImageFieldWarmer

@receiver(models.signals.post_save, sender=Image)
def warm_Person_headshot_images(sender, instance, **kwargs):
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='sizes',
        image_attr='image'
    )
    num_created, failed_to_create = person_img_warmer.warm()