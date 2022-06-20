from rest_framework import serializers

from .models import About

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer


class AboutSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = About
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)
