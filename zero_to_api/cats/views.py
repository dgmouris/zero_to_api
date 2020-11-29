from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Cat, CatBreed
from .serializers import CatBreedSerializer, CatSerializer


class CatBreedViewSet(viewsets.ModelViewSet):
    queryset = CatBreed.objects.all()
    serializer_class = CatBreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
