from .base import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--l5d1q%5=$7g034h_1pp5a-db98*x^fnxm1xm(wqco_^4lqoup'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []






# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')