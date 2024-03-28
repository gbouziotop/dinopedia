# coding=utf-8
"""Dinosaur app admin forms."""
from typing import TYPE_CHECKING

from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat

from dinosaurs.const import MAX_IMAGE_SIZE
from dinosaurs.models import Photo

if TYPE_CHECKING:
    from django.db.models.fields.files import ImageFieldFile


class PhotoInlineAdminForm(forms.ModelForm):
    """InlineAdminForm for Photo model."""

    def clean_image(self) -> 'ImageFieldFile':
        """
        Check the file size of the image.

        If file size exceeds the limit of MAX_MEDIA_SIZE raises error.
        :raises: forms.ValidationError
        :returns: The media_file.
        """
        if image := self.cleaned_data.get('image'):
            if image.size > MAX_IMAGE_SIZE:
                raise ValidationError(
                    f'Please keep filesize under {filesizeformat(MAX_IMAGE_SIZE)}, '
                    f'current filesize {filesizeformat(image.size)}'
                )
        return image

    class Meta:
        model = Photo
        fields = '__all__'
