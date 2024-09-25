from rest_framework import serializers
from .models import *
class CookieSerializer(serializers.Serializer):
    message = serializers.CharField()
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'