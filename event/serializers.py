from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from .models import Event

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

event_detail_url = HyperlinkedIdentityField(view_name='event-detail', lookup_field='slug')

class EventListSerializer(ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='sizes')
    url = event_detail_url
    class Meta:
        model = Event
        fields = ('url', 'title', 'slug', 'image', 'excerpt', 'updated_at',)


class EventDetailSerializer(ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='sizes')
    class Meta:
        model = Event
        fields = ('id', 'title', 'image', 'content', 'starts_at', 'ends_at', 'venue', 'phone', 'email', 'website', 'updated_at',)