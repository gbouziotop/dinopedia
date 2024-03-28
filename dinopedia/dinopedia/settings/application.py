# coding=utf-8
"""Dinopedia application settings."""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# allow default hosts for both local development and full development in docker-compose
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost']

ROOT_URLCONF = 'dinopedia.urls'

WSGI_APPLICATION = 'dinopedia.wsgi.application'
