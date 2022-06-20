from rest_framework import viewsets

from .models import OrganizationStructure
from .serializers import OrganizationStructureSerializer


class OrganizationStructureViewSet(viewsets.ModelViewSet):
    queryset = OrganizationStructure.objects.all()
    serializer_class = OrganizationStructureSerializer
    http_method_names = ['get']
