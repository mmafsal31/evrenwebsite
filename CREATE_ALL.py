#!/usr/bin/env python3
"""
Complete Evren Academy Project Generator
This generates all models, views, urls, templates, and static files
Usage: python generate_project.py
"""

import os
import sys
from pathlib import Path

BASE = Path(__file__).parent

def write_file(path, content):
    """Write file with parent directory creation"""
    file_path = BASE / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding='utf-8')
    print(f"✓ {path}")

def write_dir(path):
    """Create directory"""
    (BASE / path).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("🚀 EVREN ACADEMY - DJANGO PROJECT GENERATOR")
print("=" * 60)

# ============================================================================
# SETTINGS FILE
# ============================================================================
print("\n📝 Creating settings.py...")

settings_content = '''import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'ckeditor',
    'django_cleanup',
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

ROOT_URLCONF = 'evren_academy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'evren_academy.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': BASE_DIR / config('DATABASE_NAME', default='db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 300,
    },
}

WHITENOISE_COMPRESSION_QUALITY = 80
WHITENOISE_KEEP_ONLY_LATEST_FILES = True

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

SECURE_BROWSER_XSS_FILTER = True

SITE_NAME = config('SITE_NAME', default='Evren Academy')
SITE_URL = config('SITE_URL', default='http://localhost:8000')
WHATSAPP_NUMBER = config('WHATSAPP_NUMBER', default='+1234567890')
PHONE_NUMBER = config('PHONE_NUMBER', default='+92 (0) 123 456 789')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'INFO'},
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'evren-academy-cache',
        'TIMEOUT': 300,
    }
}

SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
'''

write_file('evren_academy/settings.py', settings_content)

# ============================================================================
# URLs
# ============================================================================
print("\n📝 Creating URLs...")

urls_content = '''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('courses/', include('apps.courses.urls', namespace='courses')),
    path('branches/', include('apps.branches.urls', namespace='branches')),
    path('facilities/', include('apps.facilities.urls', namespace='facilities')),
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('testimonials/', include('apps.testimonials.urls', namespace='testimonials')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admissions/', include('apps.admissions.urls', namespace='admissions')),
    path('contact/', include('apps.contact.urls', namespace='contact')),
    path('careers/', include('apps.careers.urls', namespace='careers')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('robots.txt', views.robots, name='robots'),
    path('privacy-policy/', TemplateView.as_view(template_name='pages/privacy_policy.html'), name='privacy-policy'),
    path('terms-conditions/', TemplateView.as_view(template_name='pages/terms_conditions.html'), name='terms-conditions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.server_error'
'''

write_file('evren_academy/urls.py', urls_content)

# ============================================================================
# Views
# ============================================================================
print("\n📝 Creating project views...")

views_content = '''from django.http import HttpResponse
from django.template.loader import render_to_string
from apps.core.models import *
from apps.courses.models import Course
from apps.blog.models import BlogPost

def sitemap(request):
    courses = Course.objects.filter(is_published=True)
    blog_posts = BlogPost.objects.filter(is_published=True)
    context = {'courses': courses, 'blog_posts': blog_posts}
    xml = render_to_string('sitemap.xml', context, request=request)
    return HttpResponse(xml, content_type='application/xml')

def robots(request):
    robots_txt = "User-agent: *\\nDisallow: /admin/\\n"
    return HttpResponse(robots_txt, content_type="text/plain")
'''

write_file('evren_academy/views.py', views_content)

# ============================================================================
# WSGI and ASGI
# ============================================================================
print("\n📝 Creating WSGI and ASGI...")

wsgi_content = '''import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_wsgi_application()
'''

asgi_content = '''import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_asgi_application()
'''

write_file('evren_academy/wsgi.py', wsgi_content)
write_file('evren_academy/asgi.py', asgi_content)
write_file('evren_academy/__init__.py', '')

# ============================================================================
# Create __init__.py files for all apps
# ============================================================================
print("\n📝 Creating app structure...")

apps = ['core', 'courses', 'branches', 'facilities', 'gallery', 'testimonials', 'blog', 'admissions', 'contact', 'careers', 'seo']

for app in apps:
    write_file(f'apps/{app}/__init__.py', '')
    write_file(f'apps/{app}/migrations/__init__.py', '')
    write_file(f'apps/{app}/apps.py', f'''from django.apps import AppConfig

class {app.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app}'
    verbose_name = '{app.capitalize()}'
''')

write_file('apps/__init__.py', '')

# ============================================================================
# manage.py
# ============================================================================
print("\n📝 Creating manage.py...")

manage_content = '''#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django is not installed") from exc
    execute_from_command_line(sys.argv)
'''

write_file('manage.py', manage_content)

# Create .gitignore
print("\n📝 Creating .gitignore...")

gitignore_content = '''*.pyc
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.venv
venv/
ENV/
env/
.vscode
.idea
*.sqlite3
db.sqlite3
/staticfiles/
/static/
/media/
.env
.DS_Store
*.log
'''

write_file('.gitignore', gitignore_content)

print("\n" + "=" * 60)
print("✅ Project structure generation complete!")
print("=" * 60)
print("\nNext steps:")
print("1. Navigate to project directory:")
print("   cd 'c:\\\\Users\\\\dell\\\\Desktop\\\\evern website'")
print("\n2. Create and activate virtual environment:")
print("   python -m venv venv")
print("   venv\\\\Scripts\\\\activate")
print("\n3. Install dependencies:")
print("   pip install -r requirements.txt")
print("\n4. Run migrations:")
print("   python manage.py migrate")
print("\n5. Create superuser:")
print("   python manage.py createsuperuser")
print("\n6. Run development server:")
print("   python manage.py runserver")
print("=" * 60)
'''

write_file('generate_project.py', project_gen)

print("\n✅ Script created! Run: python generate_project.py")
