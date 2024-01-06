from rest_framework.viewsets import ModelViewSet
from .serializers import  ServiceSerializer, CustomerSerializer, OrderSerializer
from .models import  ServiceModel, CustomerModel, OrderModel

class CustomerModelViewSet(ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer

class ServiceModelViewSet(ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

class OrderModelViewSet(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer