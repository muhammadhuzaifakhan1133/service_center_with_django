from rest_framework.viewsets import ModelViewSet
from .models import EmployeeModel
from .serializers import EmployeeSerializer, EmployeePutSerializer
from rest_framework.response import Response

class EmployeeModelViewSet(ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return EmployeePutSerializer
        return super().get_serializer_class()
