from .import views
from django.urls import path

urlpatterns = [
     path("add", views.CreateUpdateDeletePerson.as_view(), name="AddPerson"),
     path("update/<int:id>", views.CreateUpdateDeletePerson.as_view(), name="UpdatePerson"),
     path("delete/<int:id>", views.CreateUpdateDeletePerson.as_view(), name="DeletePerson"),
]
