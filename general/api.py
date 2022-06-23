from rest_framework import viewsets, mixins

from .models import Home
from .serializers import HomeSerializer


class HomeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
