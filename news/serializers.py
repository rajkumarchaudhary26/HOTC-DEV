from .models import News
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

news_detail_url = HyperlinkedIdentityField(view_name='news-detail', lookup_field='slug')


class NewsListSerializer(ModelSerializer):
    header_image = VersatileImageFieldSerializer(sizes=[
        ('list', 'crop__382x254'),
    ])
    url = news_detail_url

    class Meta:
        model = News
        fields = ['url', 'slug', 'title', 'excerpt', 'updated_at', 'header_image']


class NewsDetailSerializer(ModelSerializer):
    header_image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'crop__1291x967'),
    ])

    class Meta:
        model = News
        fields = ['title', 'updated_at', 'content', 'header_image']
