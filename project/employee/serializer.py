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
    document_type_id = serializers.CharField()
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['document_type_id'].required = False

    def create(self, validated_data):
        user = self.context.get("user")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        dob = validated_data.get("dob")
        document_type_id = validated_data.get("document_type_id")
        document_type_id_obj = document_type.objects.filter(id=document_type_id).first()

        if not document_type.objects.filter(id=document_type_id).exists():
            raise serializers.ValidationError({"error":"Document Type is not available"})
        
        return person.objects.create(first_name=first_name, last_name=last_name, dob=dob, document_type_id=document_type_id_obj, created_by=user)

    def update(self, instance, validated_data):

        document_type_id = validated_data.get("document_type_id")
        if not document_type_id :
            document_type_id = instance.instance.document_type_id
        
        document_type_id_obj = document_type.objects.filter(id=document_type_id).first()
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.document_type_id = document_type_id_obj if document_type_id_obj else instance.document_type_id
        instance.save()
        return instance
    
    
