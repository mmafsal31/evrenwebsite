# PythonAnywhere Deployment Guide

This project is ready for a standard PythonAnywhere Django deployment.

## 1. Upload or Pull Code

Clone or pull the repository into your PythonAnywhere account:

```bash
git clone <your-repo-url> evren-academy
cd evren-academy
```

## 2. Create Virtual Environment

```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Environment Variables

Create a `.env` file from `.env.example` and set production values:

```env
DEBUG=False
SECRET_KEY=replace-with-a-secure-key
ALLOWED_HOSTS=yourusername.pythonanywhere.com,www.yourdomain.com
SITE_URL=https://yourusername.pythonanywhere.com
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
```

## 4. Database

For SQLite:

```bash
python manage.py migrate
```

For MySQL/PostgreSQL, set `DATABASE_URL` in `.env`, then run migrations.

## 5. Static Files

```bash
python manage.py collectstatic --noinput
```

In the PythonAnywhere Web tab, map:

- Static URL: `/static/`
- Static directory: `/home/<username>/evren-academy/staticfiles`
- Media URL: `/media/`
- Media directory: `/home/<username>/evren-academy/media`

## 6. WSGI

Point the PythonAnywhere WSGI file to:

```python
import os
import sys

path = '/home/<username>/evren-academy'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'evren_academy.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 7. Admin Checklist

After deployment:

```bash
python manage.py createsuperuser
```

Then update these in Django Admin:

- Site Settings
- Hero Slides
- CTA Section
- Popup
- Courses
- Team Members
- Facilities
- Branches
- Testimonials

## 8. Final Verification

Check:

- `/`
- `/admin/`
- `/courses/`
- `/people/`
- `/contact/`
- `/sitemap.xml`
- `/robots.txt`
