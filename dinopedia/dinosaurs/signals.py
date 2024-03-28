# coding=utf-8
"""Dinosaurs app signals."""
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from dinosaurs.models import UserFavoriteDinosaurs


@receiver(post_save, sender=User, dispatch_uid='dinosaurs.receivers.create_user_favorite_dinosaurs')
def create_user_favorite_dinosaurs(sender, instance, created, *args, **kwargs) -> None:
    """Create UserFavoriteDinosaurs upon user creation."""
    if not created:
        return
    # probably doing this in a background task (celery / dramatiq) would be more suitable but was not implemented
    # due to time constraints
    UserFavoriteDinosaurs.objects.create(user=instance)
