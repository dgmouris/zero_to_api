from rest_framework import routers
from .views import CatBreedViewSet, CatViewSet

router = routers.DefaultRouter()
router.register(r'cat-breeds', CatBreedViewSet)
router.register(r'cats', CatViewSet)

urlpatterns = router.urls
