"""
Django settings for bctv2_project project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hud=a(815lc4md^grvhp_xt$8c&olr8urudsuwba4pcsusmc4z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LEAFLET_CONFIG = {
    # 'SRID': '4326',
    'DEFAULT_CENTER': (41.798959, -70.307006),
    'DEFAULT_ZOOM': 12,
    'MIN_ZOOM': 10,
    'MAX_ZOOM': 18,
    'RESET_VIEW': True,
    'ATTRIBUTION_PREFIX': 'Powered by django-leaflet',
    'SCALE': 'both',
    # 'MINIMAP': True,

    # 'PLUGINS': {
    #     'Leaflet-Coordinates': {
    #         'css': ['/static/webmap/Leaflet.Coordinates-0.1.5.css'],
    #         'js': '/static/webmap/Leaflet.Coordinates-0.1.5.src.js',
    #         'auto-include': True,
    #     },
    #     'Leaflet-Navbar': {
    #         'css': ['/static/webmap/leaflet.navbar/Leaflet.NavBar.css'],
    #         'js': '/static/webmap/leaflet.navbar/Leaflet.NavBar.js',
    #         'auto-include': True,
    #     },
    #     'Leaflet-MakiMarkers': {
    #         'css': [],
    #         'js': '/static/webmap/Leaflet.MakiMarkers.js',
    #         'auto-include': True,
    #     },
    #     'Leaflet-Providers': {
    #         'css': [],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/leaflet-providers/1.1.10/leaflet-providers.js',
    #         'auto-include': True,
    #     },
    #     'Leaflet-Ajax': {
    #         'css': [],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/leaflet-ajax/2.0.0/leaflet.ajax.min.js',
    #         'auto-include': True,
    #     },
    #     'List': {
    #         'css': [],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/list.js/1.2.0/list.min.js',
    #         'auto-include': True,
    #     },
    #     'Typeahead': {
    #         'css': [],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/typeahead.js/0.11.1/typeahead.bundle.min.js',
    #         'auto-include': True,
    #     },
    #     'Handlebars': {
    #         'css': [],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.5/handlebars.min.js',
    #         'auto-include': True,
    #     },
    #     'jquery': {
    #         'css': [],
    #         'js': 'https://code.jquery.com/jquery-2.2.4.min.js',
    #         'auto-include': True,
    #     },
    #     "nanoGallery": {
    #         'css': ['https://cdnjs.cloudflare.com/ajax/libs/nanogallery/5.10.3/css/nanogallery.min.css'],
    #         'js': 'https://cdnjs.cloudflare.com/ajax/libs/nanogallery/5.10.3/jquery.nanogallery.min.js',
    #         'auto-include': True
    #     },
    #
    # }
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "wordcount,preview,emotions,preview,spellchecker,",
    'height': "400px",
    'width': "700px",
    'theme_advanced_buttons3': "fontselect,fontsizeselect,emotions,preview,",
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bctv2_map_app',
    'leaflet',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bctv2_project.urls'

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

WSGI_APPLICATION = 'bctv2_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'bctv2',
        'USER': 'michael',
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
