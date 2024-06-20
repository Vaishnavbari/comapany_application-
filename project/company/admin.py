from django.contrib import admin
from .models import company

# Register your models here.

@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    class Meta:
        model = company
        fields = '__all__'