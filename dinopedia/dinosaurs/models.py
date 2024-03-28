# coding=utf-8
"""Dinosaurs app models."""
from colorfield.fields import ColorField
from django.conf import settings
from django.contrib.postgres.indexes import HashIndex
from django.db import models
from model_utils.fields import AutoCreatedField

from dinosaurs.const import AVERAGE_SIZE_CHOICES, EATING_CLASSIFICATION_CHOICES, PERIOD_LIVED_CHOICES


class Dinosaur(models.Model):
    name = models.CharField(max_length=30, unique=True)
    eating_classification = models.CharField(max_length=30, choices=EATING_CLASSIFICATION_CHOICES)
    typical_color = ColorField(default='#FF0000')
    period_lived = models.CharField(max_length=30, choices=PERIOD_LIVED_CHOICES)
    average_size = models.CharField(max_length=30, choices=AVERAGE_SIZE_CHOICES)
    created = AutoCreatedField()

    def __str__(self) -> str:
        """String representation."""
        return self.name

    class Meta:
        indexes = (
            HashIndex(fields=('eating_classification',)),
            HashIndex(fields=('period_lived',)),
            HashIndex(fields=('average_size',)),
        )


class Photo(models.Model):
    image = models.ImageField(upload_to='dinosaurs/photos')
    dinosaur = models.ForeignKey('Dinosaur', on_delete=models.CASCADE, related_name='photos')
    created = AutoCreatedField()

    @property
    def image_url(self) -> str:
        """Gets the image file url."""
        return self.image.url

    def __str__(self) -> str:
        """String representation."""
        return f'Image of a {self.dinosaur}'


class Like(models.Model):
    user_favorite_dinosaurs = models.ForeignKey('UserFavoriteDinosaurs', on_delete=models.CASCADE, related_name='likes')
    dinosaur = models.ForeignKey('Dinosaur', on_delete=models.CASCADE, related_name='likes')
    date_liked = AutoCreatedField()


class UserFavoriteDinosaurs(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_dinos')
    dinosaurs = models.ManyToManyField('Dinosaur', through='Like', related_name='user_favor')
    created = AutoCreatedField()

    def __str__(self):
        """String representation."""
        return f"User's {self.user_id} favorite dinosaurs"
