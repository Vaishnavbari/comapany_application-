from rest_framework import serializers
from .models import applications, application_access
from user_application.models import user_registration

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
    

class ApplicationAccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = application_access
        fields = ["application_id" , "user_id", "application_access" , "valid_from", "valid_to" , "access_type" , "access_type_value"]

    def create(self, validated_data):
        user = validated_data.get("user_id")
        application_id = validated_data.get("application_id")
        application_access = list(validated_data.get("application_access"))
        valid_from = validated_data.get("valid_from")
        valid_to = validated_data.get("valid_to")
        access_type = validated_data.get("access_type")
        access_type_value = validated_data.get("access_type_value")
        
        user_data = user_registration.objects.filter(id=user.id).first()
        if not user_data :
            raise serializers.ValidationError("User does not exist")
        
        if user_data.access_type != access_type :
            raise serializers.ValidationError(f"User access type does not match with access type {user_data.access_type}")
        
        if access_type == "company":
            for company in application_access:
                 if  "company" not in  company:
                     raise serializers.ValidationError("Access type value should be company")
                 super().create(application_id=application_id,user_id=user_data.id,application_access=company,valid_from=valid_from,valid_to=valid_to,access_type_value=access_type_value)  

        if access_type == "application":
            for application in application_access:
                 if  "application" not in  application:
                     raise serializers.ValidationError("Access type value should be app")
                 super().create(application_id=application_id,user_id=user_data,application_access=company,valid_from=valid_from,valid_to=valid_to,access_type_value=access_type_value)
        
