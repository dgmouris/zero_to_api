from django.conf.urls import url
from rest_framework import routers
from cats.views import CatTypeViewSet, CatViewSet

router = routers.DefaultRouter()
router.register(r'cat-types', CatTypeViewSet)
router.register(r'cats', CatViewSet)


urlpatterns = router.urls
