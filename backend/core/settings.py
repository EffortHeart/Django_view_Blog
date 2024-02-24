"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os, re
import environ
from pathlib import Path
from corsheaders.defaults import default_headers

# config django-environ
env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# reading .env file
# # Take environment variables from .env file

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

ADMIN_URL = 'admin/'
APPEND_SLASH = True
THOUSAND_SEPARATOR = ' '
SITE_NAME = 'Django With Vuejs Blog'
USE_THOUSAND_SEPARATOR = True
DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'flavienhugs@pm.me'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PACKAGE_APPS = [
    'django_summernote',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

CUSTOM_APPS = [
    'blog.apps.BlogConfig'
]

INSTALLED_APPS += CUSTOM_APPS + PACKAGE_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # corsherders
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': 5432,
            'ATOMIC_REQUESTS': True
        }
    }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

USE_TZ = False
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'fr'
USE_I18N = USE_L10N = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# https://docs.djangoproject.com/fr/3.2/ref/settings/#ignorable-404-urls

IGNORABLE_404_URLS = [
    re.compile(r'^/cpc/'),
    re.compile(r'^/cpanel/'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
    re.compile(r'\.(cgi|php|pl)$'),
    re.compile(r'^/apple-touch-icon.*\.png$'),
]

DISALLOWED_USER_AGENTS = [
    re.compile(r'^NaverBot.*'),
    re.compile(r'^EmailSiphon.*'),
    re.compile(r'^SiteSucker.*'),
    re.compile(r'^sohu-search'),
]

# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

# Show summernote with Bootstrap4

SUMMERNOTE_THEME = 'bs4'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '90%',
        'height': '300',
        'toolbar': [
            [
                'font', [
                    'bold', 'italic', 'underline', 'clear',
                    'strikethrough', 'superscript', 'subscript'
                ]
            ],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['height', ['height']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
        'attachment_absolute_uri': True,
        'attachment_require_authentication': True,
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'theme': 'monokai',
        },
    },
}

# django-rest-framework config
# http://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny']
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'htpp://127.0.0.1:8000',

    'http://localhost:8080',
    'htpp://127.0.0.1:8080',

    'http://localhost:3000',
    'htpp://127.0.0.1:3000',
)

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

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers) + ["contenttype"]
