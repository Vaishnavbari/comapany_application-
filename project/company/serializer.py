from rest_framework import serializers
from .models import document_type,company_provider,company


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

    company_id=serializers.PrimaryKeyRelatedField(
            queryset=company.objects.all(), write_only=True, error_messages={
            'does_not_exist': 'Company with this ID does not exist.',
            'invalid': 'Invalid value. A valid integer is required.'
        })
    provider_company_id=serializers.PrimaryKeyRelatedField(
            queryset=company.objects.all(), write_only=True, error_messages={
            'does_not_exist': 'Company provider with this ID does not exist.',
            'invalid': 'Invalid value. A valid integer is required.'
        })
    
    class Meta:
       model = company_provider
       fields = "__all__"

    # def __init__(self, instance=None,**kwargs):
    #     if self.instance:
    #         self.fields["registered_at"].required=False
    #     super().__init__(instance,**kwargs)

    def create(self, validated_data):
        user = self.context.get("user")
        company_id = validated_data.get("company_id")
        provider_company_id = validated_data.get("provider_company_id")
        registered_at = validated_data.get("registered_at")
        return company_provider.objects.create(company_id=company_id, provider_company_id=provider_company_id, registered_at=registered_at,registered_by=user, authorized_by=user)
    
    def update(self, instance, validated_data):
        user = self.context.get("user")
        instance.company_id = validated_data.get("company_id", instance.company_id)
        instance.provider_company_id = validated_data.get("provider_company_id", instance.provider_company_id)
        instance.registered_at = validated_data.get("registered_at", instance.registered_at)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        # instance.registered_by = validated_data.get("registered_by", instance.registered_by)
        # instance.authorized_by = validated_data.get("authorized_by", instance.authorized_by)
        instance.save()
        return instance