from rest_framework import viewsets

from .models import BoardMembers
from .serializers import BoardMembersSerializer


class BoardMembersViewSet(viewsets.ModelViewSet):
    queryset = BoardMembers.objects.all()
    serializer_class = BoardMembersSerializer
    http_method_names = ['get']
