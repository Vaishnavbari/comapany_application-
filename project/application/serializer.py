from rest_framework import serializers
from .models import applications, application_access
from company.models import company
from user_application.models import user_registration
import json

class ApplicationSerializers(serializers.ModelSerializer):

    class Meta:
        model = applications
        fields = "__all__"
    
    def create(self, validated_data):
        if applications.objects.filter(code=validated_data.get("code")).exists():
            raise serializers.ValidationError("Application with this code already exists")
        return applications.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if applications.objects.filter(code=validated_data.get("code")).exists():
            raise serializers.ValidationError("Application with this code already exists")
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
    

class ApplicationAccessSerializer(serializers.ModelSerializer):
    application_access = serializers.CharField()

    class Meta:
        model = application_access
        fields = ["user_id", "application_access", "valid_from", "valid_to", "access_type", "access_type_value"]

    def create(self, validated_data):
        user_id = validated_data.get("user_id")
        # application_id = validated_data.get("application_id")
        valid_from = validated_data.get("valid_from")
        valid_to = validated_data.get("valid_to")
        access_type = validated_data.get("access_type")
        access_type_value = validated_data.get("access_type_value")

        user_data = user_registration.objects.filter(id=user_id.id).first()
        if not user_data:
            raise serializers.ValidationError("User does not exist")

        application_access_list = json.loads(validated_data.get("application_access", []))

        def check_company_key(dict_list):
            return all(len(d) == 1 and 'company' in d for d in dict_list)
        
        def check_application_key(dict_list):
            return all(len(d) == 1 and 'application' in d for d in dict_list)
        
        def check_application_and_company_keys(dict_list):
            return all('application' in d and 'company' in d for d in dict_list)
        
        instances = []
    
        if access_type == "application" :

            if access_type_value == "*" :
                  
                application_name = check_application_key(application_access_list)

                if not application_name:
                    raise serializers.ValidationError("Each item in application_access should be a dictionary with 'application' key")

                for application_dict in application_access_list:
                    application_name = application_dict.get("application")
                    check_application_exist = applications.objects.filter(name=application_name)
                    if not check_application_exist.exists():
                        raise serializers.ValidationError(f"Application {application_name} does not exist")
                    application_id = check_application_exist.first()
                    instance, is_created = application_access.objects.get_or_create(
                        application_id=application_id,
                        user_id=user_data,
                        application_access=application_name,
                        valid_from=valid_from,
                        valid_to=valid_to,
                        access_type=access_type,
                        access_type_value=access_type_value
                    )
                    instances.append(instance)

            if access_type_value == "company" :
 
                check_key = check_application_and_company_keys(application_access_list)
                if not check_key:
                    raise serializers.ValidationError("Each item in application_access should be a dictionary with 'application' and 'company' ")
                
                for application_dict in application_access_list:
                    company_name = application_dict.get("company")
                    application_name = application_dict.get("application")

                    check_company_exist = company.objects.filter(legan_name=company_name) 
                    if not check_company_exist.exists():
                        raise serializers.ValidationError(f"company {company_name} does not exist ")
                    
                    check_application_exist = applications.objects.filter(name=application_name) 
                    if not check_company_exist.exists():
                        raise serializers.ValidationError(f"Application {application_name} does not exist ")
                    
                    company_id = check_company_exist.first()
                    if company_name:  
                        instance, is_created = application_access.objects.get_or_create(   
                            company_id=company_id,
                            user_id=user_data,
                            application_access=company_name,
                            valid_from=valid_from,
                            valid_to=valid_to,
                            access_type=access_type,
                            access_type_value=access_type_value
                        )
                        instances.append(instance)
                    
                    application_id = check_application_exist.first()

                    if application_name:
                        
                        instance = application_access.objects.create(
                            application_id=application_id,
                            user_id=user_data,
                            application_access=application_name,
                            valid_from=valid_from,
                            valid_to=valid_to,
                            access_type=access_type,
                            access_type_value=access_type_value
                        )
                        instances.append(instance)
    
        if access_type == "company" and access_type_value == "*":
            company_name = check_company_key(application_access_list)

            if not company_name:
                raise serializers.ValidationError("Each item in application_access should be a dictionary with 'company' key")
            
            for application_dict in application_access_list:
                company_name = application_dict.get("company")
                check_company_exist = company.objects.filter(legan_name=company_name)
                if  not check_company_exist.exists():
                    raise serializers.ValidationError(f"company {company_name} does not exist")
                company_id = check_company_exist.first()
                instance = application_access.objects.create(
                    company_id=company_id,  
                    user_id=user_data,
                    application_access=company_name,
                    valid_from=valid_from,
                    valid_to=valid_to,
                    access_type=access_type,
                    access_type_value=access_type_value
                )

                instances.append(instance)

        return instances