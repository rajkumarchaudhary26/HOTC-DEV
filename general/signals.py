from django.db import models
from django.dispatch import receiver
import ipdb

from .models import BoardMembers, OrganizationStructure, Testimonial

from versatileimagefield.image_warmer import VersatileImageFieldWarmer


@receiver(models.signals.post_save, sender=BoardMembers)
def warm_images(sender, instance, **kwargs):
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


@receiver(models.signals.post_save, sender=OrganizationStructure)
def warm_images(sender, instance, **kwargs):
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='sizes',
        image_attr='image'
    )
    num_created, failed_to_create = person_img_warmer.warm()


@receiver(models.signals.post_save, sender=Testimonial)
def warm_images(sender, instance, **kwargs):
    person_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='sizes',
        image_attr='image'
    )
    num_created, failed_to_create = person_img_warmer.warm()
