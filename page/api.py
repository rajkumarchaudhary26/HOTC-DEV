from rest_framework import viewsets, mixins

from .models import Page
from .serializers import PageSerializer


class PageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
