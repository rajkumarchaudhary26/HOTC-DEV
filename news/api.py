from rest_framework import viewsets
from .serializers import NewsDetailSerializer, NewsListSerializer
from rest_framework.filters import SearchFilter

from .models import News


class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        if self.action == 'retrieve':
            return NewsDetailSerializer