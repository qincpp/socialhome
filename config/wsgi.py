import os

from django.core.wsgi import get_wsgi_application

from config.utils import load_local_environment

load_local_environment()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
application = get_wsgi_application()
