from rest_framework.permissions import BasePermission
import jwt
from django.conf import settings
from user_application.models import user_registration
from project.utils import ExceptionHandling

class JWTAuthorization(BasePermission):
    
    @ExceptionHandling
    def authenticate(self, request):

        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            return None
        
        token = auth_header.split(" ")[-1]

        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        
        if not decoded_token:
            return None

        user_id = decoded_token["user_id"]
        user=user_registration.objects.filter(id=user_id).first()

        if not user :
            return None
        
        return user

    def has_permission(self, request, view):
        
        user = self.authenticate(request)
        request.user = user
        return user

#