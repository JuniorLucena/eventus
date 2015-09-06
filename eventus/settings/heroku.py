import dj_database_url
from base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
DATABASES = {'default': dj_database_url.config()}

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

INSTALLED_APPS = list(INSTALLED_APPS) + ['gunicorn']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
