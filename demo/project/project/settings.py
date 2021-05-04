"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

SITE_ID = os.environ.get('SITE_ID', 1)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ['127.0.0.1']

ADMINS = (
    ('Alice Bloggs', 'alice@example.com'),
)

# The IS_ADMIN_SITE setting is True with the default settings.py module and
# with the settings_adm.py module, but must be disabled with settings_pro.py.
# The settings_adm.py is used when mounting the site in a non-disclosed URL,
# available only for administration purposes.
IS_ADMIN_SITE = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'manifest_loader',
    'rest_framework',
    'avatar',
    'django_comments_xtd',
    'django_comments',

    'project',
    'users',
    'stories',
    'quotes'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('de', 'German'),
    ('it', 'Italian'),
    ('no', 'Norwegian'),
    ('ru', 'Russian'),
    ('es', 'Spanish'),
)

LANGUAGE_COOKIE_NAME = "language"

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    BASE_DIR / "static",
    # BASE_DIR / "static" / "dist",
]

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'users.User'

SIGNUP_URL          = "/user/signup/"
LOGIN_URL           = "/user/login/"
LOGOUT_URL          = "/user/logout/"
LOGIN_REDIRECT_URL  = "/"
LOGOUT_REDIRECT_URL = "/"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ]
}

COMMENTS_APP = "django_comments_xtd"

COMMENTS_XTD_CONFIRM_EMAIL = True   # Set to False to disable confirmation
COMMENTS_XTD_FROM_EMAIL = 'staff@example.com'
COMMENTS_XTD_CONTACT_EMAIL = 'staff@example.com'
COMMENTS_XTD_THREADED_EMAILS = False # default to True, use False to allow
                                     # other backend (say Celery based) send
                                     # your emails.

COMMENTS_XTD_API_USER_REPR = lambda user: user.name

COMMENTS_XTD_SALT = os.environ.get('COMMENTS_XTD_SALT', 1).encode('utf-8')
COMMENTS_XTD_SEND_HTML_EMAIL = True

# Level 3 is the maximum supported (limited by CSS classes).
COMMENTS_XTD_MAX_THREAD_LEVEL = 3  # For 'stories.story' and 'shop.articles'.

COMMENTS_XTD_MAX_THREAD_LEVEL_BY_APP_MODEL = {
    'quotes.quote': 3  # So 4 levels: from 0 to 3.
}

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'who_can_post': 'all',  # Valid values: "users", "all".
        'allow_comment_flagging': True,
        'allow_comment_reactions': True,
        'allow_object_reactions': True,
    }
}

COMMENTS_XTD_REACTIONS_ENUM = "project.enums.ReactionEnum"

AVATAR_PROVIDERS = [
    'avatar.providers.PrimaryAvatarProvider',
    'avatar.providers.GravatarAvatarProvider',
]

AVATAR_GRAVATAR_DEFAULT = "identicon"

# Depending on the action the users.edit_avatar view redirects to
# 'avatar.views.add', 'avatar.views.change', or 'avatar.views.delete'.
AVATAR_ADD_TEMPLATE = "avatar/change.html"
AVATAR_DELETE_TEMPLATE = "avatar/change.html"