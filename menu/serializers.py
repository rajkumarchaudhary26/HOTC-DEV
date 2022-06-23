from rest_framework import serializers

from .models import Menu, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('title', 'link')


class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)
    class Meta:
        model = Menu
        fields = ('name', 'menu_items')
