from .import views
from django.urls import path

urlpatterns = [
     path("add", views.CreateUpdateDeletePerson.as_view(), name="AddCompany"),
     path("update/<int:id>", views.CreateUpdateDeletePerson.as_view(), name="UpdateCompany"),
     path("delete/<int:id>", views.CreateUpdateDeletePerson.as_view(), name="DeleteCompany"),
]
