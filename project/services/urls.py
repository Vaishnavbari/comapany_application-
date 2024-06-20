from django.urls import path
from . import views

urlpatterns = [
    # Crud using company provider service category 
     path("add", views.CreateUpdateDeleteCompanyProviderServiceCategory.as_view(), name="AddCompanyServiceProvider"),
     path("update/<int:id>", views.CreateUpdateDeleteCompanyProviderServiceCategory.as_view(), name="UpdateCompanyServiceProvider"),
     path("delete/<int:id>", views.CreateUpdateDeleteCompanyProviderServiceCategory.as_view(), name="DeleteCompanyServiceProvider"),
    # Crud using  service table 
     path("add/services", views.CreateUpdateDeleteService.as_view(), name="AddService"),
     path("update/services/<int:id>", views.CreateUpdateDeleteService.as_view(), name="UpdateService"),
     path("delete/services/<int:id>", views.CreateUpdateDeleteService.as_view(), name="DeleteService"),
     
]
