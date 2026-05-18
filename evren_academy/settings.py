# evren_academy/settings.py

import os
from pathlib import Path

from decouple import config, Csv
import dj_database_url

# =========================================================
# BASE DIRECTORY
# =========================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# SECURITY
# =========================================================
SECRET_KEY = config(
    'SECRET_KEY',
    default='django-insecure-change-this-in-production'
)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost,afsalmm7.pythonanywhere.com',
    cast=Csv()
)

# =========================================================
# INSTALLED APPS
# =========================================================
INSTALLED_APPS = [
    'jazzmin',

    # Third-party apps
    'cloudinary',
    'cloudinary_storage',
    'ckeditor',
    'ckeditor_uploader',
    'django_cleanup',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'apps.core',
    'apps.courses',
    'apps.branches',
    'apps.facilities',
    'apps.gallery',
    'apps.testimonials',
    'apps.blog',
    'apps.admissions',
    'apps.contact',
    'apps.careers',
    'apps.seo',
]

# =========================================================
# MIDDLEWARE
# =========================================================
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

# =========================================================
# URLS & WSGI
# =========================================================
ROOT_URLCONF = 'evren_academy.urls'
WSGI_APPLICATION = 'evren_academy.wsgi.application'

# =========================================================
# TEMPLATES
# =========================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.site_settings',
            ],
        },
    },
]

# =========================================================
# DATABASE
# =========================================================
DATABASE_URL = config('DATABASE_URL', default='').strip()

if DATABASE_URL and DATABASE_URL != '://':
    if DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace(
            'postgres://',
            'postgresql://',
            1
        )

    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# =========================================================
# PASSWORD VALIDATION
# =========================================================
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

# =========================================================
# INTERNATIONALIZATION
# =========================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# =========================================================
# STATIC FILES
# =========================================================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Required for django-cloudinary-storage compatibility
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Django 6+ storage configuration
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# =========================================================
# MEDIA FILES
# =========================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================================================
# CLOUDINARY (OPTIONAL)
# =========================================================
USE_CLOUDINARY = config(
    'USE_CLOUDINARY',
    default=False,
    cast=bool
)

if USE_CLOUDINARY:
    DEFAULT_FILE_STORAGE = (
        'cloudinary_storage.storage.MediaCloudinaryStorage'
    )

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': config('CLOUDINARY_API_KEY'),
        'API_SECRET': config('CLOUDINARY_API_SECRET'),
    }

# =========================================================
# CKEDITOR
# =========================================================
CKEDITOR_UPLOAD_PATH = 'uploads/ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['Image', 'Table'],
            ['RemoveFormat', 'Source'],
        ],
        'height': 300,
        'width': '100%',
    }
}

# =========================================================
# EMAIL
# =========================================================
EMAIL_BACKEND = config(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend'
)

# =========================================================
# SITE SETTINGS
# =========================================================
SITE_NAME = 'Evren Academy'

SITE_URL = config(
    'SITE_URL',
    default='http://127.0.0.1:8000'
)

WHATSAPP_NUMBER = config(
    'WHATSAPP_NUMBER',
    default='+917593077179'
)

PHONE_NUMBER = config(
    'PHONE_NUMBER',
    default='+917593077179'
)

# =========================================================
# CACHE
# =========================================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 300,
    }
}

# =========================================================
# SECURITY
# =========================================================
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True

# =========================================================
# PRODUCTION HTTPS SETTINGS
# =========================================================
if not DEBUG:
    SECURE_SSL_REDIRECT = config(
        'SECURE_SSL_REDIRECT',
        default=False,
        cast=bool
    )

    SECURE_PROXY_SSL_HEADER = (
        'HTTP_X_FORWARDED_PROTO',
        'https'
    )

# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================================================
# JAZZMIN ADMIN SETTINGS
# =========================================================
JAZZMIN_SETTINGS = {
    "site_title": "Evren Academy Admin",
    "site_header": "Evren Academy",
    "site_brand": "Evren Academy",
    "welcome_sign": "Welcome to Evren Academy Admin Panel",
    "copyright": "Evren Academy",
    "show_sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "View Website", "url": "/", "new_window": True},
        {"name": "Admission Enquiries", "url": "/admin/admissions/admissionenquiry/"},
    ],
    "order_with_respect_to": [
        "core",
        "courses",
        "branches",
        "facilities",
        "admissions",
        "careers",
        "contact",
        "gallery",
        "testimonials",
        "blog",
    ],
    "icons": {
        "core.SiteSettings": "fas fa-cog",
        "core.InstitutionProfile": "fas fa-school",
        "core.HeroSlide": "fas fa-images",
        "core.Statistic": "fas fa-chart-line",
        "core.TeamMember": "fas fa-users",
        "courses.CourseCategory": "fas fa-layer-group",
        "courses.Course": "fas fa-book-open",
        "branches.Branch": "fas fa-building",
        "facilities.Facility": "fas fa-university",
        "admissions.AdmissionEnquiry": "fas fa-user-graduate",
        "careers.JobOpening": "fas fa-briefcase",
        "careers.JobApplication": "fas fa-file-signature",
        "contact.ContactMessage": "fas fa-envelope",
    },
}
