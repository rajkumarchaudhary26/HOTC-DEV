from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import Notice

notice_detail_url = HyperlinkedIdentityField(view_name='notice-detail', lookup_field='slug')

class NoticeListSerializer(ModelSerializer):
    url = notice_detail_url
    class Meta:
        model = Notice
        fields = ('url', 'title', 'updated_at',)

class NoticeDetailSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = ('title', 'content', 'updated_at', 'file',)