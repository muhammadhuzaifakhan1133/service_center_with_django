from django.db import models
from employee.models import EmployeeModel

class CustomerModel(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=45)
    city = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    lead_generated_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['employee_id'])
        ]

class ServiceModel(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['customer_id', 'service_id']),
            models.Index(fields=['service_id']),
        ]