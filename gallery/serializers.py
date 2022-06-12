from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from .models import Gallery

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

gallery_detail_url = HyperlinkedIdentityField(view_name='gallery-detail', lookup_field='gallery')

class GalleryListSerializer(serializers.ModelSerializer):
    images = VersatileImageFieldSerializer(sizes='sizes')
    url = gallery_detail_url
    class Meta:
        model = Gallery
        fields = ('url', 'title', 'images',)

    
class GalleryDetailSerializer(serializers.ModelSerializer):
    images = VersatileImageFieldSerializer(sizes='sizes')
    class Meta:
        model = Gallery
        fields = ('images',)