from rest_framework import serializers

from .models import Home

from gallery.serializers import GalleryListSerializer

class HomeSerializer(serializers.ModelSerializer):
    gallery = GalleryListSerializer(many=True)
    class Meta:
        model = Home
        fields = ('gallery', 'content', 'uploaded_at', 'updated_at',)