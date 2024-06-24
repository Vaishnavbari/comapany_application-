from django.contrib import admin
from .models import application_access,applications
# Register your models here.
admin.site.register(applications)

admin.site.register(application_access)
