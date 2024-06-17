from django.db import models
from company.models import company_provider, company,company_site
from user_application.models import user_registration
# Create your models here.
class service_category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1)
    code = models.CharField(max_length=50, unique=True)
    short_description = models.TextField(max_length=5000)
    long_description = models.TextField(max_length=50000)
    is_active = models.BooleanField(default=True)


class company_provider_service_category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1)
    company_provider_id = models.ForeignKey(company_provider, on_delete=models.CASCADE, related_name="company_provider_id")
    service_category_id = models.ForeignKey(service_category, on_delete=models.CASCADE, related_name="service_category_id")
    is_active = models.BooleanField(default=True)


class service_status(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=5000)
  

class service(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=1)
    service_uuid = models.UUIDField(max_length=50)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE, related_name="company_company_id")
    company_provider_id = models.ForeignKey(company_provider, on_delete=models.CASCADE, related_name="company_company_provider_id")
    service_category_id = models.ForeignKey(service_category, on_delete=models.CASCADE, related_name="company_service_category_id")
    company_site_id = models.ForeignKey(company_site, on_delete=models.CASCADE, related_name="company_company_site_id")
    service_status_id = models.ForeignKey(service_status, on_delete=models.CASCADE, related_name="company_service_status_id")
    prospective_start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    prospective_end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    comments = models.CharField(max_length=50)
    contact_user_id = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="company_contact_user_id")
    contact_phone =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="company_created_by_id")
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="company_modified_by_id")


