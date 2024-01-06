from rest_framework import serializers
from .models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):
    manager_id = serializers.CharField(allow_blank=True, write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmployeeModel
        exclude = ['is_staff', 'groups', 'user_permissions']


    def create(self, validated_data):
        print(validated_data)
        manager_id = validated_data.pop("manager_id", None)
        validated_data.pop("manager", None)
        if not manager_id:
            return super().create(validated_data)
        manager = EmployeeModel.objects.filter(id=manager_id).first()
        if not manager:
            raise serializers.ValidationError({"manager_id": ["Invalid manager_id"]})
        employee = EmployeeModel.objects.create(**validated_data, manager=manager)
        return employee
    
class EmployeePutSerializer(serializers.ModelSerializer):
    manager_id = serializers.CharField(allow_blank=True)
    manager = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeModel
        exclude = ['is_staff', 'groups', 'user_permissions', 'password']

    def update(self, instance, validated_data):
        manager_id = validated_data.pop("manager_id", None)
        if not manager_id:
            return super().update(instance, validated_data)
        manager = EmployeeModel.objects.filter(id=manager_id).first()
        if not manager:
            raise serializers.ValidationError({"manager_id": ["Invalid manager_id"]})
        instance.manager = manager
        return super().update(instance, validated_data)
