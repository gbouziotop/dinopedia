# coding=utf-8
"""Tests for UserRegisterViewSetV1."""
from unittest import mock

from common.testing_utils import JSONAPIViewTestCase
from dinosaurs.tests.factories import DinosaurFactory, PhotoFactory


class DinosaurViewSetV1TestCase(JSONAPIViewTestCase):
    list_url = 'api_v1:dinosaur-list'
    detail_url = 'api_v1:dinosaur-detail'

    @classmethod
    def setUpTestData(cls):
        """Set up test data."""
        cls.dino_list_url = cls.build_list_url()

    def test_authorization(self):
        """Test for the endpoint's authorization"""
        self.assert_unauthenticated_get_request_status(self.dino_list_url)

    def test_dinosaur_list(self):
        """Test dinosaur list."""
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()

        expected_data = [
            {
                'type': 'dinosaurs',
                'id': str(dino_1.id),
                'attributes': {
                    'name': dino_1.name,
                    'eatingClassification': dino_1.eating_classification,
                    'typicalColor': dino_1.typical_color,
                    'periodLived': dino_1.period_lived,
                    'averageSize': dino_1.average_size,
                    'created': mock.ANY
                },
                'relationships': {
                    'photos': {'meta': {'count': 0}, 'data': []}
                }
            },
            {
                'type': 'dinosaurs',
                'id': str(dino_2.id),
                'attributes': {
                    'name': dino_2.name,
                    'eatingClassification': dino_2.eating_classification,
                    'typicalColor': dino_2.typical_color,
                    'periodLived': dino_2.period_lived,
                    'averageSize': dino_2.average_size,
                    'created': mock.ANY
                },
                'relationships': {
                    'photos': {'meta': {'count': 0}, 'data': []}
                }
            },
        ]

        resp = self.client.get(self.dino_list_url)
        resp_json = resp.json()

        self.validate_schema_list(resp_json)
        self.assertEqual(resp_json['data'], expected_data)

    def test_dinosaur_detail(self):
        """Test dinosaur detail."""
        dino = DinosaurFactory()
        detail_url = self.build_detail_url(args=(dino.id,))

        expected_data = {
            'type': 'dinosaurs',
            'id': str(dino.id),
            'attributes': {
                'name': dino.name,
                'eatingClassification': dino.eating_classification,
                'typicalColor': dino.typical_color,
                'periodLived': dino.period_lived,
                'averageSize': dino.average_size,
                'created': mock.ANY
            },
            'relationships': {
                'photos': {'meta': {'count': 0}, 'data': []}
            }
        }

        resp = self.client.get(detail_url)
        resp_json = resp.json()

        self.validate_schema_detail(resp_json)
        self.assertEqual(resp_json['data'], expected_data)

    def test_api_get_list_include_photos(self):
        """Test dinosaur list when including photos."""
        photo = PhotoFactory()
        DinosaurFactory(photos=(photo,))
        q_data = {'include': 'photos'}
        expected = {
            'type': 'photos',
            'id': str(photo.id),
            'attributes': {
                'imageUrl': photo.image_url,
                'created': mock.ANY
            }
        }

        resp = self.client.get(self.dino_list_url, q_data)
        resp_json = resp.json()

        self.validate_schema_wth_included(resp_json)
        self.assertEqual(resp_json['included'][0], expected)

    def test_api_response_has_correct_values(self):
        """Test that the response has correct schema."""
        dino = DinosaurFactory()
        expected = {
            'links': {
                'first': mock.ANY,
                'last': mock.ANY,
                'next': mock.ANY,
                'prev': mock.ANY
            },
            'data': [
                {
                    'type': 'dinosaurs',
                    'id': str(dino.id),
                    'attributes': {
                        'name': mock.ANY,
                        'eatingClassification': mock.ANY,
                        'typicalColor': mock.ANY,
                        'periodLived': mock.ANY,
                        'averageSize': mock.ANY,
                        'created': mock.ANY
                    },
                    'relationships': {
                        'photos': mock.ANY
                    }
                }
            ],
            'meta': {
                'pagination': {
                    'page': 1,
                    'pages': 1,
                    'count': 1
                }
            }
        }

        resp = self.client.get(self.dino_list_url)
        resp_json = resp.json()

        self.assertIsNone(resp_json.get('errors'))
        self.validate_schema_list(resp_json)
        self.assertEqual(resp_json, expected)
