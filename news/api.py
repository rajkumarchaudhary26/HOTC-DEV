from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsListSerializer, NewsDetailSerializer
from rest_framework.filters import SearchFilter

from .models import News


class NewsViewset(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')
    http_method_names = ['get']
    lookup_field = 'slug'


    
