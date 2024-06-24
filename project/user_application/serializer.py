from rest_framework import serializers
from .models import user_registration
import re 
from django.contrib.auth.hashers import make_password

class UserRegistration(serializers.ModelSerializer):

    class Meta:
        model = user_registration
        fields = ['id', 'username', 'email', 'password', 'access_type', 'access_type_value']

    def validate(self, attrs):
        username = attrs.get("username")
        if self.instance is None or self.instance.username != username:
            if user_registration.objects.filter(username=username).exists():
                raise serializers.ValidationError("Username already exists")

        email = attrs.get("email")
        # if self.instance is None or self.instance.email != email:
        #     if user_registration.objects.filter(email=email).exists():
        #         raise serializers.ValidationError("Email already exists")

        password = attrs.get("password")
        if password and not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$", password):
            raise serializers.ValidationError("Password must contain at least 8 character long, 1 uppercase letter, 1 lowercase letter, and 1 number")

        access_type = attrs.get("access_type")
        access_type_value = attrs.get("access_type_value")
        
        if access_type not in ["company", "application"]:
            raise serializers.ValidationError("Access type must be either 'company', 'application' or '*'")

        if access_type == "company" and access_type_value != "*":
            raise serializers.ValidationError("If access type is company, access_type_value must be '*' ")
        
        if access_type == "application" :
            if access_type_value != "*" and access_type_value != "company" :
                raise serializers.ValidationError("If access type is application, access_type_value must be '*' or 'company' ")

        return attrs

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["password"] = make_password(validated_data.get('password')) if validated_data.get('password') else instance.password
        return super().update(instance, validated_data)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    

class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=5000)
    refresh_token = serializers.CharField(max_length=5000)

