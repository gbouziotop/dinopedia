# coding=utf-8
"""Common app api v1 views."""
from rest_framework import permissions
from rest_framework_json_api.views import ModelViewSet

from accounts.apis.v1.serializers import UserRegisterSerializerV1
from accounts.models import User


class UserRegisterViewSetV1(ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializerV1
    permission_classes = (
        permissions.AllowAny,
    )
