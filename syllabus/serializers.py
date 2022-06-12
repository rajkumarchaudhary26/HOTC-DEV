from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import Syllabus

syllabus_detail_url = HyperlinkedIdentityField(view_name='syllabus-detail', lookup_field='slug')

class SyllabusListSerializer(ModelSerializer):
    url = syllabus_detail_url
    class Meta:
        model = Syllabus
        fields = ('url', 'title', 'slug', 'excerpt', 'updated_at',)

class SyllabusDetailSerializer(ModelSerializer):
    class Meta:
        model = Syllabus
        fields = ('title', 'content', 'updated_at', 'file',)