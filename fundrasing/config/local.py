from fundrasing.settings import *

SECRET_KEY = 'development-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
