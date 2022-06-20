from rest_framework import viewsets

from .models import Download
from .serializers import DownloadSerializer


class DownloadViewSet(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    http_method_names = ['get']
