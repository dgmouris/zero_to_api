# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from cats.models import Cat, CatType


class CatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cat, CatAdmin)


class CatTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(CatType, CatTypeAdmin)
