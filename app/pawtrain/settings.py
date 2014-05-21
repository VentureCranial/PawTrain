"""
Django settings for pawtrain project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=e@uqp^l#@6xbb!n!3rg07(l$$_a=ulvbl4u^qo8r4g#rhe854'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'south',

    'gunicorn',

    'django_admin_bootstrapped', # must be before admin
    'bootstrap3',

    'django.contrib.sites',

    'django.contrib.admin',
    'django.contrib.auth',

    'passlib.ext.django',
    'oauth2_provider',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.github',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'registration',

    'django_extensions',

    'rest_framework',
    'rest_framework_swagger',

    'web',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as _template_context_processors
TEMPLATE_CONTEXT_PROCESSORS = _template_context_processors + (
    'django.core.context_processors.request',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    )


ROOT_URLCONF = 'pawtrain.urls'

WSGI_APPLICATION = 'pawtrain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pawtrain',
        'USER': 'pawtrain',
        'HOST' : '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# FORMAT_MODULE_PATH = 'pawtrain.formats'


# Use PASSLIB for support of legacy password formats. This will have
# the added benefit of automatically upgrading the strength of the hash
# for PHP accounts to the new django PBKDF2_SHA1  as well as users log in.

PASSLIB_CONFIG="""
[passlib]

schemes =
    md5_crypt, django_pbkdf2_sha256, django_pbkdf2_sha1,
    django_bcrypt, django_bcrypt_sha256, django_salted_sha1,
    django_salted_md5, django_des_crypt, hex_md5, sha512_crypt,
    bcrypt, phpass
default = django_pbkdf2_sha256
deprecated =
    django_pbkdf2_sha1, django_salted_sha1, django_salted_md5,
    django_des_crypt, hex_md5, md5_crypt
all__vary_rounds = 0.05
django_pbkdf2_sha256__min_rounds = 10000
sha512_crypt__min_rounds = 80000
staff__django_pbkdf2_sha256__default_rounds = 12500
staff__sha512_crypt__default_rounds = 100000
superuser__django_pbkdf2_sha256__default_rounds = 15000
superuser__sha512_crypt__default_rounds = 120000
"""

# django-registration vars

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7

# CORS Origin
CORS_ORIGIN_ALLOW_ALL = True

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'var/www/static/')

# Uploaded files
#
MEDIA_ROOT =  os.path.join(STATIC_ROOT, "uploads/")
MEDIA_URL = '/uploads/'



REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],

    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend', ),
    'SEARCH_PARAM': 'q',
}

SWAGGER_SETTINGS = {
    "exclude_namespaces": [],
    "api_version": '1',
    "enabled_methods": [
        'get',
    ],
    "is_authenticated": False
}

LOG_DIR = os.path.join(BASE_DIR, '..', 'var/log/pawtrain')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/debug.log',
            'maxBytes': 1024*1024*20,
            'backupCount': 7,
            'filters': ['require_debug_true'],
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/production.log',
            'maxBytes': 1024*1024*20,
            'backupCount': 7,
            'filters': ['require_debug_false'],
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/console.log',
            'maxBytes': 1024*1024*20,
            'backupCount': 7,
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': 'DEBUG',
        },
    },
}

USE_X_FORWARDED_HOST = True

SITE_ID = 1

