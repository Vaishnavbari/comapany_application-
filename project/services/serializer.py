from rest_framework import serializers
from .models import company_provider_service_category, company_provider, service_category, service,company, company_site, service_status
from user_application.models import user_registration


class CompanyProviderServiceCategorySerializer(serializers.Serializer):
    company_provider_id = serializers.PrimaryKeyRelatedField(queryset = company_provider.objects.all(),error_messages={'does_not_exist': "company provider does not exist "})
    service_category_id = serializers.PrimaryKeyRelatedField(queryset = service_category.objects.all(),error_messages={'does_not_exist': "service_category does not exist "})
    
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
    company_id = serializers.PrimaryKeyRelatedField(queryset = company.objects.all(),error_messages={'does_not_exist': "company does not exist "})
    company_provider_id = serializers.PrimaryKeyRelatedField(queryset = company_provider.objects.all(),error_messages={'does_not_exist': "company provider does not exist "})
    service_category_id = serializers.PrimaryKeyRelatedField(queryset = service_category.objects.all(),error_messages={'does_not_exist': "service category does not exist "})
    company_site_id = serializers.PrimaryKeyRelatedField(queryset = company_site.objects.all(),error_messages={'does_not_exist': "company site does not exist "})
    service_status_id = serializers.PrimaryKeyRelatedField(queryset = service_status.objects.all(),error_messages={'does_not_exist': "service does not exist "})
    prospective_start_date = serializers.DateTimeField()
    prospective_end_date = serializers.DateTimeField()
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    comments = serializers.CharField()
    contact_user_id = serializers.PrimaryKeyRelatedField(queryset = user_registration.objects.all(),error_messages={'does_not_exist': "User does not exist "})
    contact_phone = serializers.CharField()  
    created_by = serializers.PrimaryKeyRelatedField(queryset = user_registration.objects.all(),error_messages={'does_not_exist': "User does not exist "})
    modified_by = serializers.PrimaryKeyRelatedField(queryset = user_registration.objects.all(),error_messages={'does_not_exist': "User does not exist "})

    class Meta:
        model = service
        fields = "__all__"

    def create(self, validated_data):

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