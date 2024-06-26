from django.contrib import admin

# Register your models here.
from .models import company,document_type,company_provider

admin.site.register(company)
admin.site.register(document_type)