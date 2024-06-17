from django.db import models
from user_application.models import user_registration
from company.models import document_type, company, department
# Create your models here.

class position(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1) 
    code =models.CharField(max_length=5000)
    description = models.TextField(max_length=5000)


class person(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1) 
    document_type_id = models.ForeignKey(document_type, on_delete=models.CASCADE, related_name="document_type_id")
    first_name = models.CharField(max_length=5000)
    last_name = models.CharField(max_length=5000)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="created_by_user")


class employee(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1) 
    person_id = models.ForeignKey(person, on_delete=models.CASCADE, related_name="person_id")
    company_id = models.ForeignKey(company, on_delete=models.CASCADE, related_name="company_id")
    department_id = models.ForeignKey(department, on_delete=models.CASCADE, related_name="department_id")
    position_id = models.ForeignKey(position, on_delete=models.CASCADE, related_name="position_id")
    # document_type_id = models.ForeignKey(document_type, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="created_by_employee")


class employee_user(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1) 
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE, related_name="employee_id_employee")
    user_id = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="employee_id_user")
    is_active = models.BooleanField(default=True)


