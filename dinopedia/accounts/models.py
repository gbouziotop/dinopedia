# coding=utf-8
"""Accounts app models."""
from typing import Type, TYPE_CHECKING
from django.contrib.auth import get_user_model

if TYPE_CHECKING:
    from django.contrib.auth.models import User as DjangoUser

User: Type['DjangoUser'] = get_user_model()
