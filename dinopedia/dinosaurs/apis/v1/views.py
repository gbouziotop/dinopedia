# coding=utf-8
"""Keeps the API views for conversations app."""
from typing import Type, Union

from rest_framework import permissions
from rest_framework_json_api.views import ModelViewSet

from dinosaurs.apis.v1.serializers import (
    DinosaurSerializerV1, ReadUserFavoriteDinosaursSerializerV1, UpdateUserFavoriteDinosaursSerializerV1
)
from dinosaurs.models import Dinosaur, UserFavoriteDinosaurs


class DinosaurViewSetV1(ModelViewSet):
    http_method_names = ['get']
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializerV1
    permission_classes = (
        permissions.AllowAny,
    )
    _specific = ('exact', 'in')
    filterset_fields = {
        'id': _specific,
        'name': _specific,
        'eating_classification': _specific,
        'period_lived': _specific,
        'average_size': _specific,
    }
    ordering_fields = ('name', 'created')
    ordering = ('name',)

    prefetch_for_includes = {
        '__all__': ['photos']
    }


class UserFavoriteDinosaursViewSetV1(ModelViewSet):
    http_method_names = ['get', 'patch']
    queryset = UserFavoriteDinosaurs.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )
    ordering_fields = ('created',)
    ordering = ('created',)

    prefetch_for_includes = {
        'dinosaurs': ['dinosaurs__photos'],
        'dinosaurs.photos': ['dinosaurs__photos']
    }

    def get_serializer_class(self) -> Union[
        Type['UpdateUserFavoriteDinosaursSerializerV1'], Type['ReadUserFavoriteDinosaursSerializerV1']
    ]:
        """Retrieve the appropriate serializer based on the api action."""
        if self.action == 'partial_update':
            return UpdateUserFavoriteDinosaursSerializerV1
        return ReadUserFavoriteDinosaursSerializerV1

    def get_queryset(self, *args, **kwargs):
        """Override queryset to filter by requesting user."""
        if user := getattr(self.request, 'user', None):
            return super().get_queryset(*args, **kwargs).filter(user=user)
        return UserFavoriteDinosaurs.objects.none()
