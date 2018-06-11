# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CatType(models.Model):
    type_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "{}, {}".format(self.type_name, self.description)

class Cat(models.Model):
    name = models.CharField(max_length=255)
    cat_type = models.ForeignKey(CatType,
                                 on_delete=models.SET_NULL,
                                 null=True)


    def __str__(self):
        return "{}, {}".format(self.name, self.cat_type)
