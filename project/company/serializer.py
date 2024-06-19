from rest_framework import serializers
from .models import document_type


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