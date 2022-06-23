from rest_framework import serializers

from .models import Testimonial

from versatileimagefield.serializers import VersatileImageFieldSerializer


class TestimonialSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = Testimonial
        fields = ('id', 'title', 'image', 'description',
                  'created_at', 'updated_at',)