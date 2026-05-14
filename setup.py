#!/usr/bin/env python3
"""
Comprehensive setup script for Evren Academy Django Project
This script creates the entire project structure from scratch
"""

import os
import sys
from pathlib import Path

def ensure_dir(path):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)

def write_file(path, content):
    """Write content to file"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {path}")

BASE_DIR = Path(__file__).parent

# Create all directories
dirs = [
    'evren_academy',
    'apps/core/migrations',
    'apps/courses/migrations',
    'apps/branches/migrations',
    'apps/facilities/migrations',
    'apps/gallery/migrations',
    'apps/testimonials/migrations',
    'apps/blog/migrations',
    'apps/admissions/migrations',
    'apps/contact/migrations',
    'apps/careers/migrations',
    'apps/seo/migrations',
    'templates/includes',
    'templates/core',
    'templates/courses',
    'templates/branches',
    'templates/blog',
    'templates/admissions',
    'templates/contact',
    'templates/careers',
    'templates/errors',
    'static/css',
    'static/js',
    'static/images',
    'static/vendors',
    'media/uploads',
    'media/courses',
    'media/branches',
    'media/gallery',
    'media/blog',
]

print("Creating directory structure...")
for d in dirs:
    ensure_dir(BASE_DIR / d)

print("\nGenerating Python files...")

# evren_academy/__init__.py
write_file('evren_academy/__init__.py', '')

# evren_academy/wsgi.py
write_file('evren_academy/wsgi.py', '''
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_wsgi_application()
''')

# evren_academy/asgi.py
write_file('evren_academy/asgi.py', '''
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_asgi_application()
''')

# Create __init__.py files for apps
init_files = [
    'apps/__init__.py',
    'apps/core/__init__.py',
    'apps/core/migrations/__init__.py',
    'apps/courses/__init__.py',
    'apps/courses/migrations/__init__.py',
    'apps/branches/__init__.py',
    'apps/branches/migrations/__init__.py',
    'apps/facilities/__init__.py',
    'apps/facilities/migrations/__init__.py',
    'apps/gallery/__init__.py',
    'apps/gallery/migrations/__init__.py',
    'apps/testimonials/__init__.py',
    'apps/testimonials/migrations/__init__.py',
    'apps/blog/__init__.py',
    'apps/blog/migrations/__init__.py',
    'apps/admissions/__init__.py',
    'apps/admissions/migrations/__init__.py',
    'apps/contact/__init__.py',
    'apps/contact/migrations/__init__.py',
    'apps/careers/__init__.py',
    'apps/careers/migrations/__init__.py',
    'apps/seo/__init__.py',
    'apps/seo/migrations/__init__.py',
]

for init_file in init_files:
    write_file(init_file, '')

print("✅ Project structure created successfully!")
print("\nNext steps:")
print("1. cd 'c:\\Users\\dell\\Desktop\\evern website'")
print("2. python -m venv venv")
print("3. venv\\Scripts\\activate")
print("4. pip install -r requirements.txt")
print("5. python manage.py migrate")
print("6. python manage.py createsuperuser")
print("7. python manage.py runserver")
