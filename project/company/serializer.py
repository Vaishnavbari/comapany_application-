from rest_framework import serializers
from .models import document_type,company_provider,company
from company.models import *
from application.models import application_access



class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = document_type
        fields = "__all__"
    
    def create(self, validated_data):
        if document_type.objects.filter(code=validated_data.get("code")).exists():
            raise serializers.ValidationError({"code": "Document type with this code already exists."})
        return document_type.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if document_type.objects.filter(code=validated_data.get("code")).exists():
            raise serializers.ValidationError({"code": "Document type with this code already exists."})
        instance.name = validated_data.get("name", instance.name)
        instance.code = validated_data.get("code", instance.code)
        instance.abbreviation = validated_data.get("abbreviation", instance.abbreviation)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
    
class CompanyProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = company_provider

       fields = "__all__"

    def create(self, validated_data):

        user = self.context.get("user")
        company_id = validated_data.get("company_id")
        check_company = company.objects.filter(legan_name=company_id)

        if not check_company:
            raise serializers.ValidationError("company not found")
        
        user_access = application_access.objects.filter(user_id=user.id, application_access=company_id)
        if not user_access:
            raise serializers.ValidationError("you dont have access to this company")
        
        provider_company_name = validated_data.get("provider_company_id")
        check_provider = company.objects.filter(legan_name=provider_company_name)
        if not check_provider:
            raise serializers.ValidationError("provider company not found ")
        
        registered_at = validated_data.get("registered_at")

        return company_provider.objects.create(company_id=check_company.first(), provider_company_id=check_provider.first(), registered_at=registered_at, registered_by=user, authorized_by=user)
    
    def update(self, instance, validated_data):
        user = self.context.get("user")
        company_id = validated_data.get("company_id")

        check_company = company.objects.filter(legan_name=company_id)

        if not check_company:
            raise serializers.ValidationError("company not found")
        
        user_access = application_access.objects.filter(user_id=user.id, application_access=company_id)
        if not user_access:
            raise serializers.ValidationError("you dont have access to this company")
        
        provider_company_name = validated_data.get("provider_company_id")
        check_provider = company.objects.filter(legan_name=provider_company_name)
        if not check_provider:
            raise serializers.ValidationError("provider company not found ")
        
        registered_at = validated_data.get("registered_at")

        instance.provider_company_id = validated_data.get("provider_company_id", instance.provider_company_id)
        instance.registered_at = validated_data.get("registered_at", instance.registered_at)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance