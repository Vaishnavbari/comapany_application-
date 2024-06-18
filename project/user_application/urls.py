from django.urls import path
from .views import UserRegistrationView, LoginUserView,UpdateUser

urlpatterns = [
    path("register", UserRegistrationView.as_view(),name="UserRegister"),
    path("update/<int:id>", UpdateUser.as_view(),name="UserUpdate"),
    path("login", LoginUserView.as_view(),name="LoginUser")
]
