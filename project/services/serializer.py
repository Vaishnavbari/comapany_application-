from rest_framework import serializers
from .models import company_provider_service_category, company_provider, service_category, service,company, company_site, service_status
from user_application.models import user_registration


class CompanyProviderServiceCategorySerializer(serializers.Serializer):
    
    class Meta:
        model = company_provider_service_category
        fields = "__all__"

    def create(self, validated_data):
        return company_provider_service_category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.company_provider_id = validated_data.get('company_provider_id', instance.company_provider_id)
        instance.service_category_id = validated_data.get('service_category_id', instance.service_category_id)
        instance.save()
        return instance
    
class ServiceSerializer(serializers.ModelSerializer):
    prospective_start_date = serializers.DateTimeField()
    prospective_end_date = serializers.DateTimeField()
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    comments = serializers.CharField()
    contact_phone = serializers.CharField()  


    class Meta:
        model = service
        fields = "__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        company_id = validated_data.get("company_id")
        service_category_id = validated_data.get("service_category_id")
        company_site_id = validated_data.get("company_site_id")
        service_status_id = validated_data.get("service_status_id")
        prospective_start_date = validated_data.get("prospective_start_date")
        prospective_end_date = validated_data.get("prospective_end_date")
        start_datetime = validated_data.get("start_datetime")
        end_datetime = validated_data.get("end_datetime")
        comments = validated_data.get("comments")
        contact_phone = validated_data.get("contact_phone")

        # return service.objects.create(company_id=company_id,company_provider_id=user,service_category_id=service_category_id,company_site_id=company_site_id,service_status_id=service_status_id,prospective_start_date=prospective_start_date,prospective_end_date=prospective_end_date,start_datetime=start_datetime,end_datetime=end_datetime,comments=comments,contact_phone=contact_phone,created_by=user.id,modified_by=user.id)
        return service.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
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
        instance.created_by = validated_data.get("created_by", instance.created_by)
        instance.modified_by = validated_data.get("modified_by", instance.modified_by)
        instance.save()
        return instance