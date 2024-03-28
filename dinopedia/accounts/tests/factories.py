# coding=utf-8
"""Accounts app factories for tests."""
import factory

from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'Username %03d' % n)

    class Meta:
        model = User
