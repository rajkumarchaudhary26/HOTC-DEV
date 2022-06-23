from rest_framework import serializers

from .models import Page, Home
from gallery.serializers import GallerySerializer

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer


class PageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = Page
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)


class HomeSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True)

    class Meta:
        model = Home
        fields = ('gallery', 'content', 'uploaded_at', 'updated_at',)
