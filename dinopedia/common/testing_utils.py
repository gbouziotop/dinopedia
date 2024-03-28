# coding=utf-8
"""Dinopedia app utils for testing."""
from typing import Dict, List, Optional, Tuple, Union

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class APIViewTestCaseBaseWithAuth(APITestCase):
    def setUp(self) -> None:
        """Override setUp to authorize the user"""
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')


class JSONAPIViewTestCase(APITestCase):
    list_url: str = ''
    detail_url: str = ''
    content_type = 'application/vnd.api+json'

    @classmethod
    def _build_url(
            cls, url_type: str, urlconf: Optional[str] = None, args: Optional[Union[List, Tuple]] = None,
            kwargs: Optional[Dict] = None, current_app: Optional[str] = None
    ):
        """Method for building urls for requests (list | detail)."""
        if not (url := getattr(cls, f'{url_type}_url', None)):
            raise ValueError(f'You need to provide a valid {url_type} url in order to use this method')
        return reverse(url, urlconf, args, kwargs, current_app)

    @classmethod
    def build_list_url(
            cls, urlconf: Optional[str] = None, args: Optional[Union[List, Tuple]] = None,
            kwargs: Optional[Dict] = None, current_app: Optional[str] = None
    ):
        """Method for building a list url."""
        return cls._build_url('list', urlconf, args, kwargs, current_app)

    @classmethod
    def build_detail_url(
            cls, urlconf: Optional[str] = None, args: Optional[Union[List, Tuple]] = None,
            kwargs: Optional[Dict] = None, current_app: Optional[str] = None
    ):
        """Method for building a detail url."""
        return cls._build_url('detail', urlconf, args, kwargs, current_app)

    def validate_schema_list(self, json_response: Dict):
        """Validates schema of the provided json response according to the JSON API spec."""
        self.assertEqual({'links', 'data', 'meta'}, set(json_response.keys()))
        self.assertEqual({'first', 'last', 'next', 'prev'}, set(json_response['links'].keys()))
        self.assertIn('pagination', set(json_response['meta'].keys()))
        self.assertEqual({'page', 'pages', 'count'}, set(json_response['meta']['pagination'].keys()))

    def validate_schema_wth_included(self, json_response: Dict):
        """Validates schema of the provided json response included field according to the JSON API spec."""
        if not (included := json_response.get('included')):
            raise ValueError('Dont use this method if there are no included fields')
        self.assertTrue({'type', 'attributes', 'id'}.issubset(set(included[0])))

    def validate_schema_detail(
            self, json_response: Dict,
            with_relationships: Optional[bool] = False, with_meta: Optional[bool] = False
    ):
        """Validates schema of the provided json response according to the JSON API spec."""
        expected = {'data'}
        if with_meta:
            # response has the meta field
            expected.add('meta')
        self.assertEqual(expected, set(json_response.keys()))
        expected = {'type', 'id', 'attributes'}
        if with_relationships:
            expected.add('relationships')
        self.assertTrue(expected.issubset(set(json_response['data'])))

    def validate_error_schema(self, json_response: Dict):
        """Validates schema of the provided json response according to the JSON API specs for errors."""
        expected = {'errors'}
        self.assertEqual(expected, set(json_response.keys()))
        expected = {'detail', 'status', 'source', 'code'}
        for item in json_response['errors']:
            self.assertTrue(expected.issubset(set(item)))

    def assert_unauthenticated_get_request_status(self, url: str, success: Optional[bool] = True):
        """Assert the request status based on the authorization."""
        q_response = self.client.get(url, {})
        if success:
            self.assertEqual(q_response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(q_response.status_code, status.HTTP_401_UNAUTHORIZED)


class JSONAPIViewTestCaseWithAuth(APIViewTestCaseBaseWithAuth, JSONAPIViewTestCase):
    pass
