from rest_framework import serializers
from .models import  ServiceModel, CustomerModel, OrderModel
from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer

class CustomerSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField()
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = CustomerModel
        fields = "__all__"


    def create(self, validated_data):
        employee_id = validated_data.pop("employee_id", None)
        if not employee_id:
            raise serializers.ValidationError({"employee_id": ["This field may not be blank"]})
        employee = EmployeeModel.objects.filter(id=employee_id).first()
        if not employee:
            raise serializers.ValidationError({"employee_id": ["Invalid employee_id"]})
        customer = CustomerModel.objects.create(**validated_data, employee=employee)
        return customer
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(write_only=True)
    service_id = serializers.CharField(write_only=True)

    class Meta:
        model = OrderModel
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        customer_id = validated_data.pop("customer_id")
        service_id = validated_data.pop("service_id")
        customer = CustomerModel.objects.filter(id=customer_id).first()
        if not customer:
            raise serializers.ValidationError({"customer_id": ["Invalid id"]})
        service = ServiceModel.objects.filter(id=service_id).first()
        if not service:
            raise serializers.ValidationError({"service_id": ["Invalid id"]})
        order = OrderModel.objects.create(**validated_data, customer=customer, service=service)
        return order

    def update(self, instance, validated_data):
        # Validation for For Foreign Key
        customer_id = validated_data.get("customer_id")
        service_id = validated_data.get("service_id")
        customer = CustomerModel.objects.filter(id=customer_id).first()
        if not customer:
            raise serializers.ValidationError({"customer_id": ["Invalid id"]})
        service = ServiceModel.objects.filter(id=service_id).first()
        if not service:
            raise serializers.ValidationError({"service_id": ["Invalid id"]})
        return super().update(instance, validated_data)       
