from fundrasing.settings import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# If DEBUG is False, it can not serve picture
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '.craking-enigma.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST' : os.environ['MYSQL_HOST'],
        'PORT' : '3306',
    }
}
