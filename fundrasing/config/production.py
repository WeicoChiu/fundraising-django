from fundrasing.settings import *
from google.oauth2 import service_account

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

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
  os.environ['GCP_KEY_LOCATION']
)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_BUCKET_NAME = 'fundraising-static-bucket'

GS_PROJECT_ID = 'evident-axle-332911'
