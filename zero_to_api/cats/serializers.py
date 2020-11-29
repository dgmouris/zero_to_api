from .models import Cat, CatBreed

from rest_framework import serializers

class CatBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBreed
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

