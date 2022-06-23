from rest_framework import viewsets, mixins

from .models import BoardMembers, OrganizationStructure, Contact, Testimonial
from .serializers import BoardMembersSerializer, OrganizationStructureSerializer, ContactSerializer, TestimonialSerializer


class BoardMembersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = BoardMembers.objects.all()
    serializer_class = BoardMembersSerializer


class OrganizationStructureViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = OrganizationStructure.objects.all()
    serializer_class = OrganizationStructureSerializer


class ContactViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class TestimonialViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
