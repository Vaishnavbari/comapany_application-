from rest_framework import serializers
from .models import applications

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