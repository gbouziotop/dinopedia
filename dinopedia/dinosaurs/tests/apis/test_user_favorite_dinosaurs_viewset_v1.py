# coding=utf-8
"""Tests for UserRegisterViewSetV1."""
import json
from unittest import mock

from rest_framework import status

from accounts.tests.factories import UserFactory
from common.testing_utils import JSONAPIViewTestCaseWithAuth
from dinosaurs.tests.factories import DinosaurFactory


class UserFavoriteDinosaursViewSetV1TestCase(JSONAPIViewTestCaseWithAuth):
    list_url = 'api_v1:user-favorite-dinosaurs-list'
    detail_url = 'api_v1:user-favorite-dinosaurs-detail'

    @classmethod
    def setUpTestData(cls):
        """Set up test data."""
        cls.user_fav_dinos_list_url = cls.build_list_url()
        cls.user = UserFactory()

    def test_authorization(self):
        """Test for the endpoint's authorization"""
        self.assert_unauthenticated_get_request_status(self.user_fav_dinos_list_url)

    def test_user_can_only_view_his_favorites(self):
        """Test that a user can only view his favorite dinosaurs"""
        other_user = UserFactory()
        other_user.favorite_dinos.dinosaurs.set(DinosaurFactory.create_batch(2))

        resp = self.client.get(self.user_fav_dinos_list_url)
        resp_json = resp.json()

        self.assertEqual(len(resp_json['data']), 1)
        self.assertEqual(resp_json['data'][0]['id'], str(self.user.favorite_dinos.id))

    def test_dino_favorite_list(self):
        """Test list request."""
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()
        self.user.favorite_dinos.dinosaurs.set([dino_1, dino_2])

        expected_data = [
            {
                'type': 'user-favorite-dinosaurs',
                'id': str(self.user.favorite_dinos.id),
                'attributes': {
                    'created': mock.ANY
                },
                'relationships': {
                    'user': {
                        'data': {'type': 'users', 'id': str(self.user.id)}
                    },
                    'dinosaurs': {
                        'meta': {'count': 2},
                        'data': [
                            {'type': 'dinosaurs', 'id': str(dino_1.id)},
                            {'type': 'dinosaurs', 'id': str(dino_2.id)}
                        ]
                    }
                }
            }
        ]

        resp = self.client.get(self.user_fav_dinos_list_url)
        resp_json = resp.json()

        self.validate_schema_list(resp_json)
        self.assertEqual(resp_json['data'], expected_data)

    def test_dino_favorite_detail(self):
        """Test detail request."""
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()
        self.user.favorite_dinos.dinosaurs.set([dino_1, dino_2])
        detail_url = self.build_detail_url(args=(self.user.favorite_dinos.id,))

        expected_data = {
            'type': 'user-favorite-dinosaurs',
            'id': str(self.user.favorite_dinos.id),
            'attributes': {
                'created': mock.ANY
            },
            'relationships': {
                'user': {
                    'data': {'type': 'users', 'id': str(self.user.id)}
                },
                'dinosaurs': {
                    'meta': {'count': 2},
                    'data': [
                        {'type': 'dinosaurs', 'id': str(dino_1.id)},
                        {'type': 'dinosaurs', 'id': str(dino_2.id)}
                    ]
                }
            }
        }

        resp = self.client.get(detail_url)
        resp_json = resp.json()

        self.validate_schema_detail(resp_json)
        self.assertEqual(resp_json['data'], expected_data)

    def test_api_get_list_include_dinosaurs(self):
        """Test list when including dinosaurs."""
        dino = DinosaurFactory()
        self.user.favorite_dinos.dinosaurs.set([dino])
        q_data = {'include': 'dinosaurs'}
        expected = {
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

        resp = self.client.get(self.user_fav_dinos_list_url, q_data)
        resp_json = resp.json()

        self.validate_schema_wth_included(resp_json)
        self.assertEqual(resp_json['included'][0], expected)

    def test_api_get_list_include_user(self):
        """Test list when including user."""
        q_data = {'include': 'user'}
        expected = {
            'type': 'users',
            'id': str(self.user.id),
            'attributes': {
                'username': mock.ANY,
                'email': mock.ANY,
                'firstName': mock.ANY,
                'lastName': mock.ANY
            }
        }

        resp = self.client.get(self.user_fav_dinos_list_url, q_data)
        resp_json = resp.json()

        self.validate_schema_wth_included(resp_json)
        self.assertEqual(resp_json['included'][0], expected)

    def test_api_response_has_correct_values(self):
        """Test that the response has correct schema."""
        expected = {
            'links': {
                'first': mock.ANY,
                'last': mock.ANY,
                'next': mock.ANY,
                'prev': mock.ANY
            },
            'data': [
                {
                    'type': 'user-favorite-dinosaurs',
                    'id': str(self.user.favorite_dinos.id),
                    'attributes': {
                        'created': mock.ANY
                    },
                    'relationships': {
                        'user': mock.ANY,
                        'dinosaurs': mock.ANY
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

        resp = self.client.get(self.user_fav_dinos_list_url)
        resp_json = resp.json()

        self.assertIsNone(resp_json.get('errors'))
        self.validate_schema_list(resp_json)
        self.assertEqual(resp_json, expected)

    def test_dino_favorite_patch_validation_error(self):
        """Test detail request."""
        id_ = self.user.favorite_dinos.id
        detail_url = self.build_detail_url(args=(id_,))

        payload = {
            'data': {
                'type': 'user-favorite-dinosaurs',
                'id': str(id_),
                'attributes': {}
            }
        }

        resp = self.client.patch(detail_url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()
        error_dict = resp_json['errors'][0]

        self.validate_error_schema(resp_json)
        self.assertEqual(error_dict['detail'], 'Please select the kinds of dinosaurs you want to add / remove.')
        self.assertEqual(error_dict['status'], str(status.HTTP_400_BAD_REQUEST))
        self.assertEqual(error_dict['source']['pointer'], '/data/attributes/nonFieldErrors')
        self.assertEqual(error_dict['code'], 'invalid')

    def test_dino_favorite_patch_add_dinos(self):
        """Test adding dinosaurs."""
        id_ = self.user.favorite_dinos.id
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()
        detail_url = self.build_detail_url(args=(id_,))

        payload = {
            'data': {
                'type': 'user-favorite-dinosaurs',
                'id': str(id_),
                'attributes': {
                    'dinosToAdd': [dino_1.id, dino_2.id]
                }
            }
        }

        resp = self.client.patch(detail_url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()

        self.assertIsNone(resp_json.get('errors'))
        self.user.favorite_dinos.refresh_from_db()
        self.assertEqual(list(self.user.favorite_dinos.dinosaurs.all()), [dino_1, dino_2])

    def test_dino_favorite_patch_remove_dinos(self):
        """Test adding dinosaurs."""
        id_ = self.user.favorite_dinos.id
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()
        self.user.favorite_dinos.dinosaurs.set([dino_1, dino_2])
        detail_url = self.build_detail_url(args=(id_,))

        payload = {
            'data': {
                'type': 'user-favorite-dinosaurs',
                'id': str(id_),
                'attributes': {
                    'dinosToRemove': [dino_1.id, dino_2.id]
                }
            }
        }

        resp = self.client.patch(detail_url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()

        self.assertIsNone(resp_json.get('errors'))
        self.user.favorite_dinos.refresh_from_db()
        self.assertEqual(list(self.user.favorite_dinos.dinosaurs.all()), [])

    def test_dino_favorite_patch_add_remove_dinos(self):
        """Test adding and removing dinosaurs in one request."""
        id_ = self.user.favorite_dinos.id
        dino_1 = DinosaurFactory()
        dino_2 = DinosaurFactory()
        dino_3 = DinosaurFactory()
        self.user.favorite_dinos.dinosaurs.set([dino_1, dino_2])
        detail_url = self.build_detail_url(args=(id_,))

        payload = {
            'data': {
                'type': 'user-favorite-dinosaurs',
                'id': str(id_),
                'attributes': {
                    'dinosToRemove': [dino_1.id, dino_2.id],
                    'dinosToAdd': [dino_3.id]
                }
            }
        }

        resp = self.client.patch(detail_url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()

        self.assertIsNone(resp_json.get('errors'))
        self.user.favorite_dinos.refresh_from_db()
        self.assertEqual(list(self.user.favorite_dinos.dinosaurs.all()), [dino_3])
