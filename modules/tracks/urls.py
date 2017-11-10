from .views import TrackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'tracks', TrackViewSet, base_name="tracks")

urlpatterns = router.urls