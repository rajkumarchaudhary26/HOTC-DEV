from rest_framework import serializers

from .models import OrganizationStructure

from versatileimagefield.serializers import VersatileImageFieldSerializer

class OrganizationStructureSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'crop__1291x967'),
    ])
    class Meta:
        model = OrganizationStructure
        fields = ('id', 'title', 'image',)