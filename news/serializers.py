from .models import News
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

news_detail_url = HyperlinkedIdentityField(view_name='news-detail', lookup_field = 'slug')

class NewsListSerializer(ModelSerializer):
    url = news_detail_url
    class Meta:
        model = News
        fields = ('url', 'title', 'updated_at',)

class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'updated_at', 'content', 'header_image',)