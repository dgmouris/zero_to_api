from rest_framework import serializers

from cats.models import Cat, CatType


class CatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatType
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
        depth = 1
