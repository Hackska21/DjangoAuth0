from rest_framework import serializers

from apps.example.models import ExampleModel


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'


class ExampleAggregationSerializer(serializers.Serializer):
    count = serializers.IntegerField()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()