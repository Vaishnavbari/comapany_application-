# from django 
from django.shortcuts import render

# from rest_framework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# from models and serializers 
from .models import person
from employee.serializer import PersonSerializers

# from JWTAuthoriazation 
from project.JwtAuthorization import JWTAuthorization
from project.utils import ExceptionHandling

class CreateUpdateDeletePerson(APIView):

    permission_classes=[JWTAuthorization]
    
    @ExceptionHandling
    def post(self, request):
        serializer = PersonSerializers(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Person created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    @ExceptionHandling
    def put(self, request, id):
            
        person_id = person.objects.filter(id=id,created_by=request.user.id).first()

        if not person_id:
            return Response({"message": "Person not found or you dont have permission"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = PersonSerializers(instance=person_id, data=request.data, context={'user': request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Person updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    @ExceptionHandling
    def delete(self,request, id):
        person_id = person.objects.filter(id=id,created_by=request.user.id).first()
        if not person_id:
            return Response({"message": "Person not found or you dont have permission"}, status=status.HTTP_404_NOT_FOUND)
        person_id.delete()
        return Response({"message": "Person deleted successfully"}, status=status.HTTP_200_OK)
    