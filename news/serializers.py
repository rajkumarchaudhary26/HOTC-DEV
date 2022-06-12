from .models import News
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

news_detail_url = HyperlinkedIdentityField(view_name='news-detail', lookup_field='slug')


class NewsListSerializer(ModelSerializer):
    header_image = VersatileImageFieldSerializer(sizes='sizes')
    url = news_detail_url

    class Meta:
        model = News
        fields = ['url', 'slug', 'title', 'excerpt', 'updated_at', 'header_image']


class NewsDetailSerializer(ModelSerializer):
    header_image = VersatileImageFieldSerializer(sizes='sizes')

    class Meta:
        model = News
        fields = ['title', 'updated_at', 'content', 'header_image']
