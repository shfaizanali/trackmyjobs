from rest_framework import serializers
from models import ApiKey,Coords

class ApiKeySerializer(serializers.ModelSerializer):
    class Meta():
        model = ApiKey
        fields = ('api_key','current_status')

class CoordsSerializer(serializers.ModelSerializer):
    class Meta():
        user_api = ApiKeySerializer(many=True)
        model = Coords
        fields = ('user_api','coords')