# coding=utf-8
"""Tests for UserRegisterViewSetV1."""
import json

from rest_framework import status

from accounts.models import User
from common.testing_utils import JSONAPIViewTestCase


class UserRegisterViewSetV1TestCase(JSONAPIViewTestCase):
    detail_url = 'api_v1:user-register'

    @classmethod
    def setUpTestData(cls):
        """Set up test data."""
        cls.url = cls.build_detail_url()

    def test_user_register_happy_path(self):
        """Test that a user is created successfully."""
        username = 'foobiz'
        email = 'user@example.com'
        first_name = 'foo'
        last_name = 'biz'

        payload = {
            'data': {
                'type': 'users',
                'attributes': {
                    'username': 'foobiz',
                    'password': 'F123F5678',
                    'password2': 'F123F5678',
                    'email': 'user@example.com',
                    'first_name': 'foo',
                    'last_name': 'biz'
                }
            }
        }

        resp = self.client.post(self.url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()

        self.validate_schema_detail(resp_json)
        user = User.objects.get(username=username)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

    def test_user_register_unhappy_path_passwords_differ(self):
        """Test that a user is not created when passwords differ."""
        payload = {
            'data': {
                'type': 'users',
                'attributes': {
                    'username': 'foobiz',
                    'password': 'F123F5678',
                    'password2': 'F123F567811231',
                    'email': 'user@example.com',
                    'first_name': 'foo',
                    'last_name': 'biz'
                }
            }
        }

        resp = self.client.post(self.url, data=json.dumps(payload), content_type=self.content_type)
        resp_json = resp.json()
        error_dict = resp_json['errors'][0]

        self.validate_error_schema(resp_json)
        self.assertEqual(error_dict['detail'], "Password fields didn't match.")
        self.assertEqual(error_dict['status'], str(status.HTTP_400_BAD_REQUEST))
        self.assertEqual(error_dict['source']['pointer'], '/data/attributes/password')
        self.assertEqual(error_dict['code'], 'invalid')
