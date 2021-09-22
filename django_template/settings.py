import os
import json
from pathlib import Path
from django.conf.locale.ru import formats

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    with open(os.path.join(BASE_DIR, 'local', 'config.json')) as handle:
        config = json.load(handle)
except IOError:
    config = {
        'secret_key': 'simple_key',
        'db_type': 'sqlite3',
        'parser_api': 'none'
    }

try:
    with open(os.path.join(BASE_DIR, 'local', 'auth.json')) as handle:
        auth_config = json.load(handle)
except IOError:
    auth_config = {}

SECRET_KEY = str(config['secret_key'])
PARSER_API = config['parser_api']

# При False необходимо настроить nginx
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Используемые приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'section',
    'drf_yasg',
    'rest_framework',
    'config',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # TODO: Для мультиязычности.
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Настройка шаблонов
ROOT_URLCONF = 'django_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'django_template.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Настройки авторизации

AUTH_USER_MODEL = 'account.User'

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
# Swagger

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        # 'X-Access-Token': {
        #     'type': 'apiKey',
        #     'in': 'header',
        #     'name': 'X-Access-Token',
        #     'description': "TLC2B6COXFXWLSDK"
        # },
        'basic': {
            'type': 'basic'
        }
    },
}

# Настройки локализации

from django.conf.locale.ru import formats as ru_format
ru_format.DATETIME_FORMAT = "d.m.Y H:i:s"
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
gettext_noop = lambda s: s
LANGUAGES = (
    ('ru', gettext_noop('Русский')),
    ('en', gettext_noop(u'ENG')),
)
LANGUAGES_ADMIN = {
    'ru': 'Русский',
    'en': u'Английский',
}
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )
MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE
I18N_PREFIX_DEFAULT_LANGUAGE = False
ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_MESSAGES_PER_PAGE = 50


# Настройки медиа и статик файлов

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
