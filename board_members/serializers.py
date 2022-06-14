from rest_framework import serializers

from .models import BoardMembers

from versatileimagefield.serializers import VersatileImageFieldSerializer

class BoardMembersSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('square', 'crop__200x200'),
    ])
    class Meta:
        model = BoardMembers
        fields = ('id', 'name', 'image', 'designation',)