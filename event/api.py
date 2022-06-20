from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer

        if self.action == 'retrieve':
            return EventDetailSerializer
