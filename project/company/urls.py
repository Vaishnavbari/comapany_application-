from .import views
from django.urls import path

urlpatterns = [
     path("add", views.CreateUpdateDeleteDocument.as_view(), name="AddDocument"),
     path("update/<int:id>", views.CreateUpdateDeleteDocument.as_view(), name="UpdateDocument"),
     path("delete/<int:id>", views.CreateUpdateDeleteDocument.as_view(), name="DeleteDocument"),
]
