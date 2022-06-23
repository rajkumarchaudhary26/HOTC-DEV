from rest_framework import viewsets, mixins

from .models import Page, Home
from .serializers import PageSerializer, HomeSerializer


class PageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class HomeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
