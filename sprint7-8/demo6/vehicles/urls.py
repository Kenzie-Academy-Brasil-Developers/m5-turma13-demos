from .views import VehicleViewSet
from rest_framework.routers import DefaultRouter
import ipdb

router = DefaultRouter()

router.register(r"vehicles", VehicleViewSet)

urlpatterns = router.urls
# ipdb.set_trace()
