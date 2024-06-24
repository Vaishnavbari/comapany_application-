# from django 
from django.shortcuts import render

# from rest_framework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# from models and serializers 
from .models import applications
from application.serializer import ApplicationSerializers

# from JWTAuthoriazation 
from project.JwtAuthorization import JWTAuthorization
from project.utils import ExceptionHandling

# Create your views here.

class CreateUpdateDeleteApplication(APIView):

    permission_classes=[JWTAuthorization]
    
    @ExceptionHandling
    def post(self, request):
        serializer = ApplicationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Application created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    @ExceptionHandling
    def put(self, request, id):

        application_id = applications.objects.filter(id=id).first()

        if not application_id:
            return Response({"message": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ApplicationSerializers(instance=application_id,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Application updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    @ExceptionHandling
    def delete(self, request, id):
        application_id = applications.objects.filter(id=id).first()
        if not application_id:
            return Response({"message": "Application not found"}, status=status.HTTP_404_NOT_FOUND)
        application_id.delete()
        return Response({"message": "Application deleted successfully"}, status=status.HTTP_200_OK)
    