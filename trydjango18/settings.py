""" Django settings for trydjango18 project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import configparser
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Get ENV VARIABLES key
ENV_ROLE = get_env_variable('ENV_ROLE')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('TJ_SECRET_KEY')

DEBUG = False
CRMEASY_DB_PASS = False
if ENV_ROLE == 'development':
    DEBUG = True
    TJ_DB_PASS = get_env_variable('TJ_DB_PASS')

# SECURITY WARNING: don't run with debug turned on in production!

ADMINS = (("admin", "pathelius@gmail.com"),)

ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = "sgbackend.SendGridBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
SENDGRID_API_KEY = get_env_variable('SENDGRID_API_KEY')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'crispy_forms',
    'registration',
    # My apps
    'newsletter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'trydjango18.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trydjango18.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trydjango18',
        'USER': 'trydjango18',
        'PASSWORD': TJ_DB_PASS,
        'HOST': '/tmp',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'
#"/var/www/example.com/static/"

STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static"),
    #'/var/www/static/',
)

DATABASES['default'] =  dj_database_url.config()
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")
# Crispy Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Django Registration Redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_DEFAULT_FROM_EMAIL = 'pathelius@gmail.com'
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
