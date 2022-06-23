from django.db import models

from versatileimagefield.fields import VersatileImageField, PPOIField
from ckeditor.fields import RichTextField


class BoardMember(models.Model):
    name = models.CharField(max_length=50)
    image = VersatileImageField(
        upload_to='images/board_members/', null=True, blank=True, ppoi_field='ppoi')
    ppoi = PPOIField()
    designation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'board-member/{}'.format(self.name)


class OrganizationStructure(models.Model):
    title = models.CharField(max_length=255)
    image = VersatileImageField(
        upload_to='images/organization_structure/', null=True, blank=True, ppoi_field='ppoi')
    ppoi = PPOIField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Organization Structure'


class Home(models.Model):
    content = RichTextField()
    uploaded_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name_plural = 'Home'


# TODO: move to contact app
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = RichTextField()

    def __str__(self):
        return self.name


# TODO: move to testimonial app
class Testimonial(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image = VersatileImageField(
        upload_to='images/testimonial/', null=True, blank=True)
    description = RichTextField()
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
