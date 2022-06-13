from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from .models import Gallery, Image

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

gallery_detail_url = HyperlinkedIdentityField(view_name='gallery-detail', lookup_field='slug')

class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='sizes')
    class Meta:
        model = Image
        fields = ('image',)


class GalleryListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    url = gallery_detail_url

    class Meta:
        model = Gallery
        fields = ('url', 'slug', 'title', 'images',)

    
class GalleryDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = ('images',)
