#!/usr/bin/env python3
"""
EVREN ACADEMY - COMPLETE DJANGO PROJECT GENERATOR v1.0
This script creates the entire Django project with all files, models, views, and templates
Run: python BUILD_PROJECT.py
"""

import os
import sys
import json
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).parent

def write_file(rel_path, content):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content), encoding='utf-8')
    print(f"  ✓ {rel_path}")

def mkdir_p(path):
    (BASE / path).mkdir(parents=True, exist_ok=True)

print("╔" + "═" * 70 + "╗")
print("║" + " EVREN ACADEMY - DJANGO PROJECT GENERATOR ".center(70) + "║")
print("║" + " Building complete educational institution website ".center(70) + "║")
print("╚" + "═" * 70 + "╝\n")

# Create all directories
print("📁 Creating directory structure...")
dirs = [
    'evren_academy', 'apps', 'apps/core/migrations', 'apps/courses/migrations',
    'apps/branches/migrations', 'apps/facilities/migrations', 'apps/gallery/migrations',
    'apps/testimonials/migrations', 'apps/blog/migrations', 'apps/admissions/migrations',
    'apps/contact/migrations', 'apps/careers/migrations', 'apps/seo/migrations',
    'templates', 'templates/includes', 'templates/core', 'templates/courses',
    'templates/branches', 'templates/blog', 'templates/admissions', 'templates/contact',
    'templates/careers', 'templates/errors', 'templates/pages', 'static/css', 'static/js',
    'static/images', 'static/vendors', 'media/uploads', 'media/courses', 'media/branches',
    'media/gallery', 'media/blog', 'media/team',
]
for d in dirs:
    mkdir_p(d)
print("  ✓ All directories created\n")

# =========================================================================
# SETTINGS.PY
# =========================================================================
print("⚙️  Generating evren_academy/settings.py...")
write_file('evren_academy/settings.py', """
import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-12345678901234567890-change-in-prod')
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
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 300,
    },
}

WHITENOISE_COMPRESSION_QUALITY = 80
WHITENOISE_KEEP_ONLY_LATEST_FILES = True

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

SECURE_BROWSER_XSS_FILTER = True

SITE_NAME = 'Evren Academy'
SITE_URL = config('SITE_URL', default='http://localhost:8000')
WHATSAPP_NUMBER = config('WHATSAPP_NUMBER', default='+92 300 1234567')
PHONE_NUMBER = config('PHONE_NUMBER', default='+92 (0) 123 456 789')

CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache', 'TIMEOUT': 300}}
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
""")

# =========================================================================
# URLS.PY
# =========================================================================
print("⚙️  Generating evren_academy/urls.py...")
write_file('evren_academy/urls.py', """
from django.contrib import admin
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
    path('privacy-policy/', TemplateView.as_view(template_name='pages/privacy_policy.html'), name='privacy'),
    path('terms-conditions/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.server_error'
""")

# =========================================================================
# PROJECT VIEWS
# =========================================================================
print("⚙️  Generating evren_academy/views.py...")
write_file('evren_academy/views.py', """
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

def sitemap(request):
    try:
        from apps.courses.models import Course
        from apps.blog.models import BlogPost
        courses = Course.objects.filter(is_published=True)
        blog_posts = BlogPost.objects.filter(is_published=True)
        context = {'courses': courses, 'blog_posts': blog_posts}
        xml = render_to_string('sitemap.xml', context, request=request)
        return HttpResponse(xml, content_type='application/xml')
    except:
        return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>', content_type='application/xml')

def robots(request):
    return HttpResponse('User-agent: *\\nDisallow: /admin/\\nAllow: /', content_type='text/plain')
""")

# =========================================================================
# WSGI & ASGI
# =========================================================================
print("⚙️  Generating WSGI & ASGI...")
write_file('evren_academy/wsgi.py', """
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_wsgi_application()
""")

write_file('evren_academy/asgi.py', """
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_asgi_application()
""")

write_file('evren_academy/__init__.py', '')

# =========================================================================
# MANAGE.PY
# =========================================================================
print("⚙️  Generating manage.py...")
write_file('manage.py', """
#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django installation not found") from exc
    execute_from_command_line(sys.argv)
""")

# =========================================================================
# Create APP INIT FILES
# =========================================================================
print("📦 Creating app packages...")
apps = ['core', 'courses', 'branches', 'facilities', 'gallery', 'testimonials', 'blog', 'admissions', 'contact', 'careers', 'seo']

for app in apps:
    write_file(f'apps/{app}/__init__.py', '')
    write_file(f'apps/{app}/migrations/__init__.py', '')
    write_file(f'apps/{app}/apps.py', f'from django.apps import AppConfig\nclass {app.capitalize()}Config(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.{app}"\n    verbose_name = "{app.capitalize()}"\n')

write_file('apps/__init__.py', '')

# =========================================================================
# .GITIGNORE
# =========================================================================
print("📝 Creating .gitignore...")
write_file('.gitignore', """
*.pyc
__pycache__/
*.py[cod]
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
.venv
venv/
env/
.vscode
.idea
*.sqlite3
db.sqlite3
/staticfiles/
/media/
.env
.DS_Store
*.log
""")

print("\n" + "═" * 72)
print("✅ Phase 1 COMPLETE: Core project structure generated!")
print("═" * 72)
print("\n🎯 Next Steps:")
print("   1. Open new terminal in project directory")
print("   2. Create virtual environment: python -m venv venv")
print("   3. Activate: venv\\Scripts\\activate (Windows) or source venv/bin/activate")
print("   4. Install requirements: pip install -r requirements.txt")
print("   5. Then run: python BUILD_MODELS_AND_VIEWS.py")
print("\n" + "═" * 72)

