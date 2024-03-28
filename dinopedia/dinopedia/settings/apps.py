# coding=utf-8
"""Dinopedia apps settings."""

# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsAppConfig',
    'common.apps.CommonAppConfig',
    'dinosaurs.apps.DinosaursAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'colorfield',
    'rest_framework',
    'rest_framework_json_api',
]
