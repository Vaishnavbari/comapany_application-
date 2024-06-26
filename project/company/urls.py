from .import views
from django.urls import path

urlpatterns = [
     # CRUD by using document type table
     path("add", views.CreateUpdateDeleteDocument.as_view(), name="AddDocument"),
     path("update/<int:id>", views.CreateUpdateDeleteDocument.as_view(), name="UpdateDocument"),
     path("delete/<int:id>", views.CreateUpdateDeleteDocument.as_view(), name="DeleteDocument"),
      # CRUD by using company table
     path("add/company-providers", views.CreateUpdateDeleteCompanyProvider.as_view(), name="AddCompanyProvider"),
     path("update/company-provider/<int:id>", views.CreateUpdateDeleteCompanyProvider.as_view(), name="UpdateCompanyProvider"),
     path("delete/company-provider/<int:id>", views.CreateUpdateDeleteCompanyProvider.as_view(), name="DeleteCompanyProvider"),
]