import os
from pathlib import Path
# settings.py
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-je)jbxrkl0n+@*5x4_nrwoo=s7uc2v(^eci&@3ot+&#d)&z(-r'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_summernote',
    'news',
    'django_celery_results',
    'mapwidgets',
    'django.contrib.gis',
    'leaflet',
    # 'django.contrib.gisleaflet',
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

ROOT_URLCONF = 'news_project.urls'
GDAL_LIBRARY_PATH = os.path.join('C:\\OSGeo4W', 'bin', 'gdal310.dll')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'news_project', 'templates'),  # Указываем путь к папке templates
        ],
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

WSGI_APPLICATION = 'news_project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Constance configuration
INSTALLED_APPS += ('constance', 'constance.backends.database')
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
TIME_ZONE = 'Asia/Krasnoyarsk'
CELERY_TIMEZONE = 'Asia/Krasnoyarsk'

CONSTANCE_CONFIG = {
    'NEWSLETTER_SUBJECT': ('Тема рассылки', 'string'),
    'NEWSLETTER_MESSAGE': ('Сообщение рассылки', 'string'),
    'NEWSLETTER_RECIPIENTS': ('mangowillgoodboy.com', 'kogneva108@gmail.com'),
}


LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_TZ = True
GEOS_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\geos_c.dll'  # Использование двойных слэшей

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Используем in-memory брокер для тестирования (не рекомендуется для production)
CELERY_BROKER_URL = 'redis://localhost:6380/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'


# SMTP настройки для Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mangowillgoodboy@gmail.com'
EMAIL_HOST_PASSWORD = 'dcqd jpli zsmi sbrr'
DEFAULT_FROM_EMAIL = 'mangowillgoodboy@gmail.com'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {  # или можно настроить конкретный логгер, например 'news.tasks'
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'news.tasks': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (55.76, 37.64),
    'DEFAULT_ZOOM': 13,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 20,
    'SCALE': 'metric',
    'ATTRIBUTION_PREFIX': 'Powered by Django-Leaflet',
    'TILES': [
        ('OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            'attribution': 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
            'maxZoom': 19,
        }),
    ],
}
