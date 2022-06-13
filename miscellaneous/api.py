from rest_framework import viewsets

from .models import Miscellaneous
from .serializers import MiscellaneousListSerializer, MiscellaneousDetailSerializer


class MiscellaneousViewSet(viewsets.ModelViewSet):
    queryset = Miscellaneous.objects.all()
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return MiscellaneousListSerializer
        if self.action == 'retrieve':
            return MiscellaneousDetailSerializer