# coding=utf-8
"""Dinosaurs app api v1 serializers."""
from typing import Dict

from rest_framework_json_api import serializers

from dinosaurs.models import Dinosaur, Photo, UserFavoriteDinosaurs


class DinosaurSerializerV1(serializers.ModelSerializer):
    included_serializers = {
        'photos': 'dinosaurs.apis.v1.serializers.PhotoSerializerV1'
    }

    class Meta:
        model = Dinosaur
        resource_name = 'dinosaurs'
        _read_only_fields = (
            'name', 'eating_classification', 'typical_color', 'period_lived', 'average_size', 'created', 'photos'
        )
        fields = _read_only_fields
        read_only_fields = _read_only_fields


class PhotoSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Photo
        resource_name = 'photos'
        _read_only_fields = ('image_url', 'created')
        fields = _read_only_fields
        read_only_fields = _read_only_fields


class ReadUserFavoriteDinosaursSerializerV1(serializers.ModelSerializer):
    included_serializers = {
        'user': 'accounts.apis.v1.serializers.UserSerializerV1',
        'dinosaurs': 'dinosaurs.apis.v1.serializers.DinosaurSerializerV1'
    }

    class Meta:
        model = UserFavoriteDinosaurs
        resource_name = 'user-favorite-dinosaurs'
        _read_only_fields = ('user', 'dinosaurs', 'created')
        fields = _read_only_fields
        read_only_fields = _read_only_fields


class UpdateUserFavoriteDinosaursSerializerV1(ReadUserFavoriteDinosaursSerializerV1):
    dinos_to_add = serializers.ListField(child=serializers.IntegerField(min_value=1), write_only=True, required=False)
    dinos_to_remove = serializers.ListField(child=serializers.IntegerField(min_value=1), write_only=True, required=False)

    def validate(self, attrs) -> Dict:
        """Override validate to verify that dinosaurs to be added / removed have been sent."""
        if not attrs.get('dinos_to_add') and not attrs.get('dinos_to_remove'):
            raise serializers.ValidationError('Please select the kinds of dinosaurs you want to add / remove.')
        return attrs

    def update(self, instance, validated_data) -> 'UserFavoriteDinosaurs':
        """Partial update a UserFavoriteDinosaurs object."""
        if dinos_to_add := validated_data.get('dinos_to_add'):
            instance.dinosaurs.add(*dinos_to_add)
        if dinos_to_remove := validated_data.get('dinos_to_remove'):
            instance.dinosaurs.remove(*dinos_to_remove)
        return instance

    class Meta(ReadUserFavoriteDinosaursSerializerV1.Meta):
        fields = ReadUserFavoriteDinosaursSerializerV1.Meta.fields + ('dinos_to_add', 'dinos_to_remove')
