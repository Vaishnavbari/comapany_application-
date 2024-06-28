from rest_framework import serializers
from employee.models import person

class PersonSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_by = serializers.CharField(required=False)
    class Meta:
        model = person
        fields = "__all__"
    
    def create(self, validated_data):
        user = self.context.get("user")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        dob = validated_data.get("dob")
        document_type_id = validated_data.get("document_type_id")
        persons, is_created = person.objects.create(first_name=first_name, last_name=last_name, dob=dob, document_type_id=document_type_id, created_by=user)
        return persons
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.document_type_id = validated_data.get('document_type_id', instance.document_type_id)
        instance.save()
        return instance
    
    
