# coding=utf-8
"""Dinopedia app utils."""
from rest_framework_json_api.schemas.openapi import AutoSchema, SchemaGenerator


class DinoPediaSchemaGenerator(SchemaGenerator):
    def get_schema(self, request=None, public=False):
        """Override get_schema to add authentication for Swagger UI."""
        schema = super().get_schema(request, public)
        schema['components']['securitySchemes'] = {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer'
            }
        }
        schema['security'] = [
            {'BearerAuth': []}
        ]
        return schema


class AutoSchemaWithIncludeAndSort(AutoSchema):
    def _get_sort_parameters(self, path, method):
        """Sort parameter: https://jsonapi.org/format/#fetching-sorting."""
        ordering_fields = list(getattr(self.view, 'ordering_fields', []))
        ordering_reverse_fields = [f'-{field}' for field in ordering_fields]
        return [{
            'name': 'sort',
            'in': 'query',
            'description': 'Array of fields to sort by. Add `-` to sort by descending order',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'string',
                    'enum': ordering_fields + ordering_reverse_fields
                },
            },
            'style': 'form',
            'explode': False
        }]

    def _get_include_parameters(self, path, method):
        """Includes parameter: https://jsonapi.org/format/#fetching-includes."""
        serializer = self.get_serializer(path, method)
        if included_serializers := getattr(serializer, 'included_serializers', None):
            available_includes = list(included_serializers.keys())
            return [{
                'name': 'include',
                'in': 'query',
                'description': 'Array of fields to include',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'string',
                        'enum': available_includes
                    }
                },
                'style': 'form',
                'explode': False
            }]
        return super()._get_include_parameters(path, method)
