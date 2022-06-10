from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import NewsListSerializer, NewsDetailSerializer

from .models import News

class NewsView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = News.objects.all()
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        if self.action == 'retrieve':
            return NewsDetailSerializer