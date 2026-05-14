#!/usr/bin/env python3
"""
MASTER INITIALIZATION SCRIPT - Run this immediately after installing requirements
This will initialize the complete Evren Academy project in one command.

Usage: python INITIALIZE.py
"""

import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent

def print_header(text):
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)

def print_step(num, text):
    print(f"\n[Step {num}] {text}")
    print("-" * 80)

def run_command(cmd, description):
    print(f"  Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode != 0:
        print(f"  ⚠️  Warning: Command may have had issues")
    return result.returncode == 0

print_header(" EVREN ACADEMY - MASTER INITIALIZATION SCRIPT ")
print("\nThis script will initialize your Django project completely.")
print("Ensure you have:")
print("  ✓ Python 3.13+")
print("  ✓ Virtual environment activated")
print("  ✓ Requirements installed (pip install -r requirements.txt)")

# Step 1: Generate project structure
print_step(1, "Generating project structure with models and views")
if os.path.exists('COMPLETE_BUILD.py'):
    exec(open('COMPLETE_BUILD.py').read())
else:
    print("  ✗ COMPLETE_BUILD.py not found!")
    sys.exit(1)

# Step 2: Run migrations
print_step(2, "Creating database and running migrations")
run_command(['python', 'manage.py', 'makemigrations'], 'Make migrations')
run_command(['python', 'manage.py', 'migrate'], 'Migrate database')

# Step 3: Generate templates
print_step(3, "Generating templates and static files")
if os.path.exists('BUILD_TEMPLATES.py'):
    exec(open('BUILD_TEMPLATES.py').read())
else:
    print("  ✗ BUILD_TEMPLATES.py not found!")

# Step 4: Collect static files
print_step(4, "Collecting static files")
run_command(['python', 'manage.py', 'collectstatic', '--noinput'], 'Collect static')

# Final summary
print_header(" ✅ INITIALIZATION COMPLETE! ")

print("\n🎯 NEXT STEPS:\n")

print("1. Create Superuser Account:")
print("   python manage.py createsuperuser\n")

print("2. Run Development Server:")
print("   python manage.py runserver\n")

print("3. Access in Browser:")
print("   Frontend:  http://localhost:8000")
print("   Admin:     http://localhost:8000/admin\n")

print("4. Customize Content:")
print("   • Login to admin panel")
print("   • Add site settings (logo, colors, contact info)")
print("   • Add hero slides")
print("   • Add courses, branches, team members")
print("   • Add testimonials and blog posts\n")

print("=" * 80)
print("  For detailed documentation, see: README.md and SETUP_GUIDE.md")
print("=" * 80 + "\n")
