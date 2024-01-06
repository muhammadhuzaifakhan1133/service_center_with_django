from rest_framework.routers import DefaultRouter
from .views import  ServiceModelViewSet, CustomerModelViewSet, OrderModelViewSet

router = DefaultRouter()
router.register("customer", CustomerModelViewSet)
router.register("service", ServiceModelViewSet)
router.register("order", OrderModelViewSet)

urlpatterns = [] + router.urls