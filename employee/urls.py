from rest_framework.routers import DefaultRouter
from .views import EmployeeModelViewSet

router = DefaultRouter()
router.register("employee", EmployeeModelViewSet)

urlpatterns = [] + router.urls