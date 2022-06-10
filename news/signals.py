from django.db import models
from django.dispatch import receiver

from .models import News

from versatileimagefield.image_warmer import VersatileImageFieldWarmer

@receiver(models.signals.post_save, sender=News)
def warm_Person_headshot_images(sender, instance, **kwargs):
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='news_headers',
        image_attr='header_image'
    )
    num_created, failed_to_create = person_img_warmer.warm()