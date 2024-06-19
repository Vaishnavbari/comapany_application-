from django.db import models
from user_application.models import user_registration

# Create your models here.
class document_type(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1) 
    code = models.CharField(unique=True, max_length=50)
    abbreviation = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)


class company(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1) 
    document_type_id = models.ForeignKey(document_type, on_delete=models.CASCADE,related_name="document_type")
    id_number = models.CharField(max_length=50, blank=True, null=True)
    legan_name = models.CharField(max_length=50, blank=True, null=True)
    commercial_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True) 


class site_category(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1) 
    code = models.CharField(max_length=50 , unique=True)
    short_description = models.TextField(max_length=5000 , unique=True)
    description = models.TextField(max_length=50000 , unique=True)


class company_site(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE, related_name="company_id_company_site")
    site_category_id = models.ForeignKey(site_category, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=50 , unique=True)
    details = models.TextField(max_length=5000 , unique=True)
    is_active = models.BooleanField(default=True)


class department(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1)
    code = models.CharField(max_length=50 , unique=True)
    description = models.TextField(max_length=5000 , unique=True)


class company_provider(models.Model):
    # id = models.IntegerField(primary_key=True, unique=True, default=1)
    company_id =models.ForeignKey(company, on_delete=models.CASCADE, related_name="company_id_by")
    provider_company_id = models.ForeignKey(company, on_delete=models.CASCADE, related_name="provider_company_id")
    is_active =models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    registered_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="company_provider_registered_by")
    authorized_by = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name="company_provider_authorized_by")


