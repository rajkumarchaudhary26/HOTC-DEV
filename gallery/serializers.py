from email.mime import image
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from .models import Gallery, Image

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

gallery_detail_url = HyperlinkedIdentityField(view_name='gallery-detail', lookup_field='slug')

class ListImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('list', 'crop__382x254'),
    ])
    class Meta:
        model = Image
        fields = ('id', 'image',)

class DetailImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'crop__1291x967'),
    ])
    class Meta:
        model = Image
        fields = ('id', 'image',)


class GalleryListSerializer(serializers.ModelSerializer):
    images = ListImageSerializer(many=True)
    url = gallery_detail_url

    class Meta:
        model = Gallery
        fields = ('url', 'slug', 'title', 'images',)

    
class GalleryDetailSerializer(serializers.ModelSerializer):
    images = DetailImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = ('images',)