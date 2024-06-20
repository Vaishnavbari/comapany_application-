from django.shortcuts import render
from .models import company_provider_service_category, service
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CompanyProviderServiceCategorySerializer, ServiceSerializer
from rest_framework import status
from project.JwtAuthorization import JWTAuthorization

# Create your views here.
class CreateUpdateDeleteCompanyProviderServiceCategory(APIView):

    permission_classes=[JWTAuthorization]

    def post(self, request):
        serializer = CompanyProviderServiceCategorySerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Company provider created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    def put(self, request, id):
            
        data_id = company_provider_service_category.objects.filter(id=id).first()

        if not data_id:
            return Response({"message": "Company_provider service category not found "}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = CompanyProviderServiceCategorySerializer(instance=data_id, data=request.data, context={'user': request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "company_provider service category updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        
        data_id = company_provider_service_category.objects.filter(id=id).first()

        if not data_id:
            return Response({"message": "Company_provider service category not found "}, status=status.HTTP_404_NOT_FOUND)
        
        data_id.delete()
        return Response({"message": "Company_provider service category deleted successfully"}, status=status.HTTP_200_OK)
    
class CreateUpdateDeleteService(APIView):

    permission_classes=[JWTAuthorization]

    def post(self, request):
        serializer = ServiceSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Service created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    def put(self, request, id):
            
        data_id = service.objects.filter(id=id).first()

        if not data_id:
            return Response({"message": "Service not found "}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = ServiceSerializer(instance=data_id, data=request.data, context={'user': request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Service updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        
        data_id = service.objects.filter(id=id).first()

        if not data_id:
            return Response({"message": "Service not found "}, status=status.HTTP_404_NOT_FOUND)
        
        data_id.delete()
        return Response({"message": "Service deleted successfully"}, status=status.HTTP_200_OK)