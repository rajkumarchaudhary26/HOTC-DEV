from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Syllabus
from .serializers import SyllabusDetailSerializer, SyllabusListSerializer


class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return SyllabusListSerializer
        if self.action == 'retrieve':
            return SyllabusDetailSerializer
