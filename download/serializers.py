from dataclasses import field
import os

from rest_framework import serializers

from .models import Download


class DownloadSerializer(serializers.ModelSerializer):
    myfile = serializers.FileField(source='file', use_url=False)
    class Meta:
        model = Download
        fields = ('title', 'myfile')
