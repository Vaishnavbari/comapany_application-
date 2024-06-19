from django.urls import path
from  . import views

urlpatterns = [
     path("add", views.CreateUpdateDeleteApplication.as_view(), name="AddApplications"),
     path("update/<int:id>", views.CreateUpdateDeleteApplication.as_view(), name="UpdateApplications"),
     path("delete/<int:id>", views.CreateUpdateDeleteApplication.as_view(), name="DeleteApplications"),
]
   
