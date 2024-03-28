# coding=utf-8
"""Dinosaur app admin form tests."""
from unittest import mock

from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.test import TestCase

from dinosaurs.admin.forms import PhotoInlineAdminForm
from dinosaurs.const import MAX_IMAGE_SIZE
from dinosaurs.tests.factories import PhotoFactory


class PhotoInlineAdminFormTestCase(TestCase):
    """Tests for PhotoInlineAdminForm."""

    def test_clean_image_valid(self):
        """Test that an image is cleaned - happy path."""
        photo = PhotoFactory()

        form = PhotoInlineAdminForm(instance=photo)

        form.is_valid()
        form.cleaned_data = {'image': photo.image}

        self.assertEqual(form.clean_image(), photo.image)

    @mock.patch('django.db.models.fields.files.ImageFieldFile.size', new_callable=mock.PropertyMock)
    def test_clean_image_invalid(self, mock_size):
        """Test that an image is cleaned - unhappy path."""
        mock_size.return_value = MAX_IMAGE_SIZE + 1
        photo = PhotoFactory()

        form = PhotoInlineAdminForm(instance=photo)

        form.is_valid()
        form.cleaned_data = {'image': photo.image}

        with self.assertRaises(ValidationError) as cm:
            form.clean_image()

        expected_error_message = f'Please keep filesize under {filesizeformat(MAX_IMAGE_SIZE)}, ' \
                                 f'current filesize {filesizeformat(MAX_IMAGE_SIZE + 1)}'
        self.assertEqual(cm.exception.message, expected_error_message)
