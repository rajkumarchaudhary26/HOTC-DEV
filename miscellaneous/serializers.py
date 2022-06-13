from .models import Miscellaneous, MiscellaneousImage
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

miscellaneous_detail_url = HyperlinkedIdentityField(view_name='miscellaneous-detail', lookup_field='slug')

class MiscellaneousImageSerializer(ModelSerializer):
    class Meta:
        model = MiscellaneousImage
        fields = ('id', 'image',)


class MiscellaneousListSerializer(ModelSerializer):
    url = miscellaneous_detail_url
    class Meta:
        model = Miscellaneous
        fields = ('url', 'title',)

class MiscellaneousDetailSerializer(ModelSerializer):
    images = VersatileImageFieldSerializer(sizes='sizes')
    images = MiscellaneousImageSerializer(many=True)
    class Meta:
        model = Miscellaneous
        fields = ('title', 'images', 'updated_at',)
