from rest_framework import viewsets, mixins

from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
