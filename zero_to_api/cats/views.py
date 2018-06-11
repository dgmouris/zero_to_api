# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets, permissions

from cats.models import Cat, CatType
from cats.serializers import CatTypeSerializer, CatSerializer


class CatTypeViewSet(viewsets.ModelViewSet):
    queryset = CatType.objects.all()
    serializer_class = CatTypeSerializer


class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
