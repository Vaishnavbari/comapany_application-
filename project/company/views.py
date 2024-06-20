# from django 
from django.shortcuts import render

# from rest_framework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# from models and serializers 
from .models import document_type, company_provider
from company.serializer import DocumentTypeSerializer, CompanyProviderSerializer

# from JWTAuthoriazation 
from project.JwtAuthorization import JWTAuthorization

# Create your views here.

class CreateUpdateDeleteDocument(APIView):

    # permission_classes = [JWTAuthorization]

    def post(self, request):
        serializer = DocumentTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Document created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    def put(self, request, id):

        document_type_id = document_type.objects.filter(id=id).first()

        if not document_type_id:
            return Response({"message": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DocumentTypeSerializer(instance=document_type_id, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Document updated successfully", "data":serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        document_type_id = document_type.objects.filter(id=id).first()
        if not document_type_id:
            return Response({"message": "Document not found"}, status=status.HTTP_404_NOT_FOUND)
        document_type_id.delete()
        return Response({"message": "Document deleted successfully"}, status=status.HTTP_200_OK)


class CreateUpdateDeleteCompanyProvider(APIView):

    permission_classes=[JWTAuthorization]

    def post(self, request):
        serializer = CompanyProviderSerializer(data=request.data, context={"user":request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Company created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
    
    def put(self, request, id):
        company_provider_id = company_provider.objects.filter(id=id,registered_by=request.user).first()
        if not company_provider_id:
            return Response({"message": "Company not found or Unauthorized"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CompanyProviderSerializer(data=request.data, instance=company_provider_id, context={"user":request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"Company update successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)

    def delete(self,request,id):
        company_provider_id = company_provider.objects.filter(id=id,registered_by=request.user).first()
        if not company_provider_id:
            return Response({"message": "Company not found or Unauthorized"}, status=status.HTTP_404_NOT_FOUND)
        company_provider_id.delete()
        return Response({"message": "Company deleted successfully"}, status=status.HTTP_200_OK)
                            