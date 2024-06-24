from django.urls import path
from .views import UserRegistrationView, LoginUserView,UpdateUser, PermissionGrantingView

urlpatterns = [
    path("register", UserRegistrationView.as_view(),name="UserRegister"),
    path("update/<int:id>", UpdateUser.as_view(),name="UserUpdate"),
    path("login", LoginUserView.as_view(),name="LoginUser"),
    path("permission/grant",PermissionGrantingView.as_view(), name="permission")
]
