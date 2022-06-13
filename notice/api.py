from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from .models import Notice
from .serializers import NoticeDetailSerializer, NoticeListSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'content')
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return NoticeListSerializer
        if self.action == 'retrieve':
            return NoticeDetailSerializer
    
class LatestNotice(ListAPIView):
    serializer_class = NoticeListSerializer
    
    def get_queryset(self):
        return Notice.objects.filter().order_by('-created_at')[:3]