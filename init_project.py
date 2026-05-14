#!/usr/bin/env python
"""
Script to initialize the Evren Academy Django project structure.
Run this script after creating the virtual environment and installing requirements.
"""

import os
import sys
import shutil
from pathlib import Path

def create_directory(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"✓ Created: {path}")

def create_file(path, content=""):
    """Create a file with content."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created: {path}")

def main():
    base_path = Path(__file__).parent
    
    print("🚀 Initializing Evren Academy Django Project...\n")
    
    # Create directory structure
    dirs = [
        'evren_academy',
        'apps/core',
        'apps/core/migrations',
        'apps/core/management/commands',
        'apps/courses',
        'apps/courses/migrations',
        'apps/courses/management/commands',
        'apps/branches',
        'apps/branches/migrations',
        'apps/branches/management/commands',
        'apps/facilities',
        'apps/facilities/migrations',
        'apps/gallery',
        'apps/gallery/migrations',
        'apps/testimonials',
        'apps/testimonials/migrations',
        'apps/blog',
        'apps/blog/migrations',
        'apps/blog/management/commands',
        'apps/admissions',
        'apps/admissions/migrations',
        'apps/contact',
        'apps/contact/migrations',
        'apps/careers',
        'apps/careers/migrations',
        'apps/seo',
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
    
    for dir_path in dirs:
        create_directory(base_path / dir_path)
    
    # Create __init__.py files for Python packages
    init_files = [
        'apps/__init__.py',
        'apps/core/__init__.py',
        'apps/courses/__init__.py',
        'apps/branches/__init__.py',
        'apps/facilities/__init__.py',
        'apps/gallery/__init__.py',
        'apps/testimonials/__init__.py',
        'apps/blog/__init__.py',
        'apps/admissions/__init__.py',
        'apps/contact/__init__.py',
        'apps/careers/__init__.py',
        'apps/seo/__init__.py',
    ]
    
    for init_file in init_files:
        create_file(base_path / init_file)
    
    # Create migration __init__.py files
    migration_dirs = [
        'apps/core/migrations/__init__.py',
        'apps/courses/migrations/__init__.py',
        'apps/branches/migrations/__init__.py',
        'apps/facilities/migrations/__init__.py',
        'apps/gallery/migrations/__init__.py',
        'apps/testimonials/migrations/__init__.py',
        'apps/blog/migrations/__init__.py',
        'apps/admissions/migrations/__init__.py',
        'apps/contact/migrations/__init__.py',
        'apps/careers/migrations/__init__.py',
        'apps/seo/migrations/__init__.py',
    ]
    
    for migration_dir in migration_dirs:
        create_file(base_path / migration_dir)
    
    print("\n✅ Project structure initialized successfully!")
    print("\nNext steps:")
    print("1. Run: python manage.py migrate")
    print("2. Run: python manage.py createsuperuser")
    print("3. Run: python manage.py collectstatic")
    print("4. Run: python manage.py runserver")

if __name__ == '__main__':
    main()
