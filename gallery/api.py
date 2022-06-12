from rest_framework import viewsets

from .models import Gallery
from .serializers import GalleryListSerializer, GalleryDetailSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return GalleryListSerializer
        if self.action == 'retrieve':
            return GalleryDetailSerializer