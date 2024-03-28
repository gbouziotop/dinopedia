# coding=utf-8
"""Dinosaurs app config."""
from django.apps import AppConfig


class DinosaursAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dinosaurs'

    def ready(self):
        """Override ready to connect signals to callbacks."""
        from . import signals  # noqa
