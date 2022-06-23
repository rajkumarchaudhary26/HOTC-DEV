from rest_framework import viewsets, mixins

from .models import Miscellaneous, Download
from .serializers import MiscellaneousListSerializer, MiscellaneousDetailSerializer, DownloadSerializer


class MiscellaneousListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Miscellaneous.objects.all()
    serializer_class = MiscellaneousListSerializer
    lookup_field = 'slug'


class MiscellaneousDetailViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Miscellaneous.objects.all()
    serializer_class = MiscellaneousDetailSerializer
    lookup_field = 'slug'


class DownloadViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
