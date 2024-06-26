from django.contrib import admin
from .models import service_category, company_site, service_status
from company.models import site_category

# Register your models here.
@admin.register(service_category)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','code','short_description',"long_description","is_active"]


@admin.register(company_site)
class CompanySiteAdmin(admin.ModelAdmin):
    list_display = ['company_id','site_category_id','name',"details","is_active"]
    

@admin.register(service_status)
class ServiceStatusAdmin(admin.ModelAdmin):
   list_display = ['code','description']


# @admin.register(company_provider)
# class CompanyProviderAdmin(admin.ModelAdmin):
#     list_display = ['company_id', 'provider_company_id', 'registered_at', "registered_by", "authorized_by"]


@admin.register(site_category)
class SiteCategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'short_description', 'description']