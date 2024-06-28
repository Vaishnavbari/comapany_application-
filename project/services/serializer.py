from rest_framework import serializers
from .models import company_provider_service_category, company_provider, service,company
from application.models import application_access

class CompanyProviderServiceCategorySerializer(serializers.Serializer):
    company_name = serializers.CharField(write_only=True)
    service_category_code = serializers.CharField()
    provider_company_name = serializers.CharField(write_only=True)

    class Meta:
        model = company_provider_service_category
        fields = ['company_name', 'service_category_code', 'provider_company_name']

    def create(self, validated_data):
        user = self.context.get("user")
        company_name = validated_data.get("company_name")
        service_category_code = validated_data.get("service_category_code")
        provider_company_name = validated_data.get("provider_company_name")

        check_company = company.objects.filter(legan_name=company_name).first()
        if not check_company:
            raise serializers.ValidationError("Company not found")

        user_access = company_provider.objects.filter(registered_by=user.id, provider_company_id__legan_name=provider_company_name).first()
        if not user_access:
            raise serializers.ValidationError("You don't have access to this company")

        return company_provider_service_category.objects.create(
            company_provider_id=user_access, 
            service_category_code=service_category_code
        )
    
    def update(self, instance, validated_data):
        user = self.context.get("user")
        company_name = validated_data.get("company_name")
        service_category_code = validated_data.get("service_category_code")
        provider_company_name = validated_data.get("provider_company_name")

        check_company = company.objects.filter(legan_name=company_name).first()
        if not check_company:
            raise serializers.ValidationError("Company not found")

        user_access = company_provider.objects.filter(registered_by=user.id, provider_company_id__legan_name=provider_company_name).first()
        if not user_access:
            raise serializers.ValidationError("You don't have access to this company")
        
        instance.company_provider_id = validated_data.get('company_provider_id', instance.company_provider_id)
        instance.service_category_code = validated_data.get('service_category_code', instance.service_category_code)
        instance.save()
        return instance
    
class ServiceSerializer(serializers.ModelSerializer):
    prospective_start_date = serializers.DateTimeField()
    prospective_end_date = serializers.DateTimeField()
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    comments = serializers.CharField()
    contact_phone = serializers.CharField()
    created_by = serializers.CharField(required=False)
    modified_by = serializers.CharField(required=False)

    class Meta:
        model = service
        fields = "__all__"
    
    def create(self, validated_data):
        user=self.context.get("user")
        company_id = validated_data.get("company_id")
        if company_id :
            check_company = company.objects.filter(id=company_id.id).first()
            if not check_company:
                raise serializers.ValidationError("Company not found")
            
        company_provider_id = validated_data.get("company_provider_id")
    
        check_company_permission = application_access.objects.filter(company_id=company_id.id, user_id=user.id)
        if not check_company_permission:
            raise serializers.ValidationError("You don't have access to this company")
        
        check_company_provider = company_provider.objects.filter(company_id=company_id.id)
        if not check_company_provider:
            raise serializers.ValidationError("Company provider not found")
        
        service_category_id = validated_data.get("service_category_id")
        company_site_id = validated_data.get("company_site_id")
        service_status_id = validated_data.get("service_status_id")
        prospective_start_date = validated_data.get("prospective_start_date")
        prospective_end_date = validated_data.get("prospective_end_date")
        start_datetime = validated_data.get("start_datetime")
        end_datetime = validated_data.get("end_datetime")
        comments = validated_data.get("comments")
        contact_phone = validated_data.get("contact_phone")
        return service.objects.create(company_id=check_company, company_provider_id=company_provider_id, service_category_id=service_category_id, company_site_id=company_site_id,service_status_id=service_status_id, prospective_start_date=prospective_start_date, prospective_end_date=prospective_end_date, start_datetime=start_datetime, end_datetime=end_datetime,comments=comments, contact_phone=contact_phone, contact_user_id=user, created_by=user)
    
    def update(self, instance, validated_data):
        user=self.context.get("user")
        company_id = validated_data.get("company_id")
        if company_id:
            check_company_permission = application_access.objects.filter(company_id=company_id.id, user_id=user.id)
            if not check_company_permission:
                raise serializers.ValidationError("You don't have access to this company")
            
            check_company_provider = company_provider.objects.filter(company_id=company_id.id)
            if not check_company_provider:
                raise serializers.ValidationError("Company provider not found")
                
        instance.company_id = validated_data.get("company_id", instance.company_id)
        instance.company_provider_id = validated_data.get("company_provider_id", instance.company_provider_id)
        instance.service_category_id = validated_data.get("service_category_id", instance.service_category_id)
        instance.company_site_id = validated_data.get("company_site_id", instance.company_site_id)
        instance.service_status_id = validated_data.get("service_status_id", instance.service_status_id)
        instance.prospective_start_date = validated_data.get("prospective_start_date", instance.prospective_start_date)
        instance.prospective_end_date = validated_data.get("prospective_end_date", instance.prospective_end_date)
        instance.start_datetime = validated_data.get("start_datetime", instance.start_datetime)
        instance.end_datetime = validated_data.get("end_datetime", instance.end_datetime)
        instance.comments = validated_data.get("comments", instance.comments)
        instance.contact_user_id = validated_data.get("contact_user_id", instance.contact_user_id)
        instance.contact_phone = validated_data.get("contact_phone", instance.contact_phone)
        instance.modified_by = validated_data.get(user, instance.modified_by)
        instance.save()
        return instance