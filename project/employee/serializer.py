from rest_framework import serializers
from .models import person
from company.models import document_type
from user_application.models import user_registration 
from datetime import datetime


class PersonSerializers(serializers.Serializer):
    

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    created_at = serializers.DateTimeField(required=False)
    

    def create(self, validated_data):
        print(validated_data)
        
        user = self.context.get("user")
    
        if not document_type.objects.filter(id=validated_data.get("document_type_id")).exists():
            raise serializers.ValidationError({"error":"Document Type is not available"})
        return person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.document_type_id = validated_data.get('document_type_id', instance.document_type_id)
        instance.document_number = validated_data.get('document_number', instance.document_number)
        instance.save()
        return instance
    
    
