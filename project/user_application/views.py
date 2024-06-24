# from django 
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render

# from rest_framework 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# from models and serializers 
from .serializer import UserRegistration, LoginSerializer, TokenSerializer
from .models import user_registration,Token
from application.models import application_access
from application.serializer import ApplicationAccessSerializers

# others
from project.JwtAuthorization import JWTAuthorization
from project.utils import ExceptionHandling



# Create your views here.
def get_tokens_for_user(user):
    """Generate access token and refresh token"""
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    
    @ExceptionHandling
    def post(self, request):
        serializer = UserRegistration(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"user registered successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)


class UpdateUser(APIView):

    permission_classes = [JWTAuthorization]

    @ExceptionHandling 
    def put(self, request, id):
        user = user_registration.objects.filter(id=id).first()
        if not user:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        if user != request.user or request.user.is_superuser != True:
            return Response({"message": "You dont have an permission"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserRegistration(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"user updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    

class LoginUserView(APIView):

    @ExceptionHandling
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get('username')
        password = serializer.data.get('password')
        
        if not username or not password:
            return Response({"message": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({'errors': {'non_field_errors': ['username or password not found..!']}}, status=status.HTTP_404_NOT_FOUND)
        
        token = get_tokens_for_user(user)

        login(request, user)
         
        SerializeToken=Token.objects.create(access_token=token.get("access"),refresh_token=token.get("refresh"), user=user)

        return Response({'message':'Login Successful..!', 'token':TokenSerializer(SerializeToken).data}, status=status.HTTP_200_OK)
    

class PermissionGrantingView(APIView):
    
    # permission_classes = [JWTAuthorization]

    def post(self, request):
        serializer = ApplicationAccessSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Permission granted successfully"}, status=status.HTTP_201_CREATED)
