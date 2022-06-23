from rest_framework import viewsets, mixins

from .models import Menu
from .serializers import MenuSerializer


class MenuViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Menu.objects.all().prefetch_related('menu_items')
    serializer_class = MenuSerializer