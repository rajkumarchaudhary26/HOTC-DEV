from rest_framework import serializers

from .models import Home
from gallery.serializers import GallerySerializer


class HomeSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True)

    class Meta:
        model = Home
        fields = ('gallery', 'content', 'uploaded_at', 'updated_at',)
