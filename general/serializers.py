from rest_framework import serializers

from .models import BoardMembers, OrganizationStructure, Contact, Testimonial

from versatileimagefield.serializers import VersatileImageFieldSerializer


class BoardMembersSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('square', 'crop__200x200'),
    ])

    class Meta:
        model = BoardMembers
        fields = ('id', 'name', 'image', 'designation',)


class OrganizationStructureSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = OrganizationStructure
        fields = ('id', 'title', 'image',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'message',)


class TestimonialSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = Testimonial
        fields = ('id', 'title', 'image', 'description',
                  'created_at', 'updated_at',)
