from rest_framework import serializers

from .models import Download


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = ('title', 'file',)
