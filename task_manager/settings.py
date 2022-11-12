"""
Django settings for task_manager project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import rollbar
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv("SECRET_KEY")
# SECRET_KEY = 'django-insecure-1%p(cujr9n#*30rnw)egot2!pkxl-u4=nwa+*h95dq-=83*qbo'
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEBUG = True
ALLOWED_HOSTS = ['webserver',
                 '0.0.0.0',
                 '127.0.0.1',
                 'task-manager-ikonnikova.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task_manager',
    'bootstrap4',
    'task_manager.apps.users',
    'task_manager.apps.statuses',
    'task_manager.apps.tasks',
    'task_manager.apps.labels',
    'django_filters',
    'rollbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
]

ROLLBAR_KEY = os.getenv("ROLLBAR_KEY")
# ROLLBAR_KEY = 'a6b53c16037f45ee9ca52dc6d44007d3'
ROLLBAR = {
    'access_token': ROLLBAR_KEY,
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}

rollbar.init(**ROLLBAR)

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'task_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

my_db = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(my_db)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'task_manager', 'locale'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
        },
        'rollbar': {
            'filters': ['require_debug_false'],
            'access_token': ROLLBAR_KEY,
            'environment': 'production',
            'class': 'rollbar.logger.RollbarHandler'
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", 'rollbar'],
            "level": "INFO",
            "propagate": True
        },
        "task_manager": {
            "handlers": ["console", 'rollbar'],
            "level": "DEBUG",
            "propagate": True
        },
    }
}
