import json

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import CV

class CVSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = CV
        fields = ['id', 'user', 'title', 'data', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['data'] = json.loads(instance.data)
        return representation
