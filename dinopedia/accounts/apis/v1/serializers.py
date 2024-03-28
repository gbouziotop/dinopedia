# coding=utf-8
"""Common app api v1 serializers."""
from typing import Dict

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_json_api import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from accounts.models import User


class UserRegisterSerializerV1(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        resource_name = 'users'
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs) -> Dict:
        """Override validate to verify passowrd."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def create(self, validated_data) -> 'User':
        """Create a User object."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class JSONAPITokenBaseSerializer(serializers.Serializer):
    class Meta:
        resource_name = 'tokens'


# create token serializers that are json api compatible
class JSONAPITokenObtainPairSerializer(JSONAPITokenBaseSerializer, TokenObtainPairSerializer):
    pass


class JSONAPITokenRefreshSerializer(JSONAPITokenBaseSerializer, TokenRefreshSerializer):
    pass


class UserSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = User
        resource_name = 'users'
        _read_only_fields = ('username', 'email', 'first_name', 'last_name')
        fields = _read_only_fields
        read_only_fields = _read_only_fields
