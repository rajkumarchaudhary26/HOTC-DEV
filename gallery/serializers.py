from email.mime import image
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from .models import Gallery, Image

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

gallery_detail_url = HyperlinkedIdentityField(view_name='gallery-detail', lookup_field='slug')


class GallerySerializer(serializers.ModelSerializer):
    url = gallery_detail_url
    featured_image = VersatileImageFieldSerializer(sizes=[
        ('list', 'thumbnail__382x254'),
    ])
    class Meta:
        model = Gallery
        fields = ('id', 'url', 'title', 'slug', 'featured_image',)


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])
    class Meta:
        model = Image
        fields = ('image',)
    
class GalleryDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'images',)