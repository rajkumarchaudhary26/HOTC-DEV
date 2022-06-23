from rest_framework import serializers

from .models import Page

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer


class PageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = Page
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)
