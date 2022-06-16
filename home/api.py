from rest_framework import viewsets

from .models import Home
from .serializers import HomeSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    http_method_names = ['get']