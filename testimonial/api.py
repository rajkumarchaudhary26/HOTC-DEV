from rest_framework import viewsets, mixins

from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer