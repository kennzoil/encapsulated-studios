"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zmy6wx(b-b7^=&c42qz-5agt2e+#$p$14y4yu%()5h25qkk7@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Applications installed in our project
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # modules from requirements.txt
    'bootstrap4',
    'pipeline',
    # internal applications
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TODO - change this to match <project_name>.urls
ROOT_URLCONF = 'encapsulated-studios.urls'

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

# TODO - change this to match <project_name>.wsgi.application
WSGI_APPLICATION = 'encapsulated-studios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


if DEBUG:
    DATABASES = {
        # TODO - change db name to <database_name>
        'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'encapsulated', }
    }
else:
    DATABASES = {
        'default': dj_database_url.config()
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# django-pipeline configuration

PIPELINE = {}

PIPELINE['COMPILERS'] = (
    'pipeline.compilers.es6.ES6Compiler',
    'pipeline.compilers.sass.SASSCompiler',
)


# Static files (CSS, JavaScript, Images)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_NAME = 'app'
STATIC_URL = '/static/'
# location of destination for collected static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(APP_NAME, 'static'),
]

# Simplified static file serving.
# https://django-pipeline.readthedocs.io/en/latest/installation.html
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())