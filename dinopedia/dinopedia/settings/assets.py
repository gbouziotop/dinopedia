# coding=utf-8
"""Dinopedia static asset settings."""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
from .env import SECRETS_MEDIA_ROOT, SECRETS_STATIC_ROOT

STATIC_ROOT = SECRETS_STATIC_ROOT
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


MEDIA_ROOT = SECRETS_MEDIA_ROOT
MEDIA_URL = 'media/'
