from rest_framework import serializers
from core.models import Screen


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ["id", "address", "resolution", "diagonal"]
