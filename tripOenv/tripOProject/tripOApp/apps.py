
import sys
from urllib.parse import urlparse

from django.apps import AppConfig
from django.conf import settings


class TripoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tripOApp'
