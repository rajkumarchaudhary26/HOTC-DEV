from .models import Miscellaneous, MiscellaneousImage
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

# Third-party packages
from versatileimagefield.serializers import VersatileImageFieldSerializer

miscellaneous_detail_url = HyperlinkedIdentityField(
    view_name='miscellaneous-detail', lookup_field='slug')


class ListMiscellaneousImageSerializer(ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('list', 'thumbnail__382x254'),
    ])

    class Meta:
        model = MiscellaneousImage
        fields = ('id', 'image',)
    
class DetailMiscellaneousImageSerializer(ModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[
        ('detail', 'thumbnail__1291x967'),
    ])

    class Meta:
        model = MiscellaneousImage
        fields = ('id', 'image',)


class MiscellaneousListSerializer(ModelSerializer):
    url = miscellaneous_detail_url

    class Meta:
        model = Miscellaneous
        fields = ('url', 'title',)


class MiscellaneousDetailSerializer(ModelSerializer):
    # import ipdb; ipdb.set_trace()
    images = DetailMiscellaneousImageSerializer(many=True)

    class Meta:
        model = Miscellaneous
        fields = ('title', 'images', 'updated_at',)