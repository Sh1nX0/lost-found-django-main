import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ваш-секретный-ключ-здесь'  # Замените на свой или используйте переменные окружения

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Разрешенные хосты
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Доверенные источники для CSRF (решение вашей ошибки)
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://localhost:8000',
    'http://127.0.0.1:8000',
    'https://127.0.0.1:8000',
    'http://localhost:3000',  # Для React/Vue фронтенда
    'https://localhost:3000',
]

# Настройки CSRF
CSRF_COOKIE_SECURE = False  # Для разработки, в продакшене должно быть True
CSRF_COOKIE_HTTPONLY = False  # Разрешить доступ через JavaScript
CSRF_COOKIE_SAMESITE = 'Lax'  # Или 'None' для кросс-доменных запросов
CSRF_USE_SESSIONS = False  # Хранить CSRF токен в cookie (по умолчанию)
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'  # Стандартная вьюха для ошибок CSRF

# Настройки сессий
SESSION_COOKIE_SECURE = False  # Для разработки
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Или 'cache', 'file'

# Настройки CORS (если используете отдельный фронтенд)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'https://localhost:8000',
    'http://localhost:3000',
    'https://localhost:3000',
    'http://127.0.0.1:3000',
    'https://127.0.0.1:3000',
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Ваши приложения
    # 'myapp',
    
    # Сторонние приложения
    # 'corsheaders',  # Если используете CORS
    # 'rest_framework',  # Если используете DRF
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # ВАЖНО: этот middleware должен быть включен
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Дополнительные middleware
    # 'corsheaders.middleware.CorsMiddleware',  # Если используете CORS (должен быть перед CommonMiddleware)
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Добавьте свои директории с шаблонами
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # Для PostgreSQL:
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'mydatabase',
    #     'USER': 'mydatabaseuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'ru-ru'  # или 'en-us'

TIME_ZONE = 'Europe/Moscow'  # или 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Для collectstatic
STATICFILES_DIRS = [BASE_DIR / 'static']  # Ваши статические файлы

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для Django REST Framework (если используете)
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ],
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ],
# }

# Настройки для разработки с React/Vue (если используете)
if DEBUG:
    # Дополнительные настройки для разработки
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    
    # Упрощенные настройки CSRF для разработки
    CSRF_COOKIE_DOMAIN = None
    CSRF_COOKIE_PATH = '/'
    
    # Для отладки SQL запросов
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            },
        },
    }