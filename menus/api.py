from rest_framework import viewsets, mixins

from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer