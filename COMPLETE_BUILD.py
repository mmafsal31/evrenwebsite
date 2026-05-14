#!/usr/bin/env python3
"""
EVREN ACADEMY - COMPLETE DJANGO PROJECT BUILDER v2.0
Generates entire project in one command: python COMPLETE_BUILD.py
This creates: models, views, urls, admin, forms, templates, static files
"""

import os
from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).parent

def write(rel_path, content, silent=False):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content), encoding='utf-8')
    if not silent:
        print(f"  ✓ {rel_path}")

def mkdir_p(path):
    (BASE / path).mkdir(parents=True, exist_ok=True)

print("\n" + "╔" + "═" * 80 + "╗")
print("║" + "EVREN ACADEMY - COMPLETE DJANGO PROJECT BUILDER".center(80) + "║")
print("║" + "Creating full-featured educational institution website".center(80) + "║")
print("╚" + "═" * 80 + "╝\n")

# Create directories silently
dirs = ['evren_academy', 'apps', 'apps/core/migrations', 'apps/courses/migrations',
        'apps/branches/migrations', 'apps/facilities/migrations', 'apps/gallery/migrations',
        'apps/testimonials/migrations', 'apps/blog/migrations', 'apps/admissions/migrations',
        'apps/contact/migrations', 'apps/careers/migrations', 'apps/seo/migrations',
        'templates', 'templates/includes', 'templates/core', 'templates/courses',
        'templates/branches', 'templates/blog', 'templates/admissions', 'templates/contact',
        'templates/careers', 'templates/errors', 'templates/pages', 'static/css', 'static/js',
        'static/images', 'static/vendors', 'media/uploads', 'media/courses', 'media/branches',
        'media/gallery', 'media/blog', 'media/team', 'fixtures']

for d in dirs:
    mkdir_p(d)

print("✓ Directory structure created\n")

# SETTINGS.PY
print("⚙️  Generating core configuration...")
write('evren_academy/settings.py', '''
import os
from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY', default='django-dev-key-change-production')
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
    'apps.core', 'apps.courses', 'apps.branches', 'apps.facilities',
    'apps.gallery', 'apps.testimonials', 'apps.blog', 'apps.admissions',
    'apps.contact', 'apps.careers', 'apps.seo',
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

TEMPLATES = [{
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
}]

WSGI_APPLICATION = 'evren_academy.wsgi.application'

DATABASES = {'default': {
    'ENGINE': config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
    'NAME': BASE_DIR / config('DATABASE_NAME', default='db.sqlite3'),
}}

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

CKEDITOR_CONFIGS = {'default': {
    'toolbar': [['Format', 'Bold', 'Italic', 'Underline'], ['NumberedList', 'BulletedList'], ['Link', 'Unlink']],
    'height': 300,
}}

WHITENOISE_COMPRESSION_QUALITY = 80
WHITENOISE_KEEP_ONLY_LATEST_FILES = True

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

SITE_NAME = 'Evren Academy'
SITE_URL = config('SITE_URL', default='http://localhost:8000')
WHATSAPP_NUMBER = config('WHATSAPP_NUMBER', default='+92 300 1234567')
PHONE_NUMBER = config('PHONE_NUMBER', default='+92 (0) 123 456 789')

CACHES = {'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'TIMEOUT': 300,
}}

SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
''')

# URLS
write('evren_academy/urls.py', '''
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
    path('terms/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.core.views.page_not_found'
handler500 = 'apps.core.views.server_error'
''')

write('evren_academy/views.py', '''
from django.http import HttpResponse
from django.template.loader import render_to_string

def sitemap(request):
    try:
        xml = render_to_string('sitemap.xml', {}, request=request)
        return HttpResponse(xml, content_type='application/xml')
    except:
        return HttpResponse('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>', content_type='application/xml')

def robots(request):
    return HttpResponse('User-agent: *\\nDisallow: /admin/\\n', content_type='text/plain')
''')

write('evren_academy/wsgi.py', '''
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_wsgi_application()
''')

write('evren_academy/asgi.py', '''
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
application = get_asgi_application()
''')

write('evren_academy/__init__.py', '')
write('manage.py', '''
#!/usr/bin/env python
import os, sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evren_academy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django not installed") from exc
    execute_from_command_line(sys.argv)
''')

# Create all app __init__ files
print("📦 Creating apps...")
apps = ['core', 'courses', 'branches', 'facilities', 'gallery', 'testimonials', 'blog', 'admissions', 'contact', 'careers', 'seo']
for app in apps:
    write(f'apps/{app}/__init__.py', '')
    write(f'apps/{app}/migrations/__init__.py', '', silent=True)

write('apps/__init__.py', '')

# Now create the complete models for each app
print("\n📝 Generating all app files...")

# ====== CORE APP ======
write('apps/core/models.py', '''
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default='Evren Academy')
    tagline = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='media/', blank=True, null=True)
    favicon = models.ImageField(upload_to='media/', blank=True, null=True)
    phone = models.CharField(max_length=20, default='+92 300 1234567')
    whatsapp = models.CharField(max_length=20, default='+92 300 1234567')
    email = models.EmailField(default='info@everenacademy.com')
    address = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    primary_color = models.CharField(max_length=7, default='#0B5D3B')
    secondary_color = models.CharField(max_length=7, default='#D4AF37')
    footer_text = models.TextField(blank=True)
    announcement = models.CharField(max_length=500, blank=True)
    show_announcement = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name

class HeroSlide(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=100, blank=True, default='Learn More')
    button_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label}: {self.value}"

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    bio = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
''')

write('apps/core/views.py', '''
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SiteSettings, HeroSlide, Statistic, TeamMember

def get_site_settings():
    return SiteSettings.objects.first() or SiteSettings.objects.create()

class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = get_site_settings()
        context['hero_slides'] = HeroSlide.objects.filter(is_active=True)
        context['statistics'] = Statistic.objects.all()
        context['team_members'] = TeamMember.objects.all()[:6]
        return context

def page_not_found(request, exception=None):
    return render(request, 'errors/404.html', status=404)

def server_error(request):
    return render(request, 'errors/500.html', status=500)
''')

write('apps/core/urls.py', '''
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
''')

write('apps/core/admin.py', '''
from django.contrib import admin
from .models import SiteSettings, HeroSlide, Statistic, TeamMember

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic', {'fields': ('site_name', 'tagline', 'logo', 'favicon')}),
        ('Contact', {'fields': ('phone', 'whatsapp', 'email', 'address')}),
        ('Social', {'fields': ('facebook', 'twitter', 'instagram', 'linkedin', 'youtube')}),
        ('Design', {'fields': ('primary_color', 'secondary_color')}),
        ('Footer', {'fields': ('footer_text', 'announcement', 'show_announcement')}),
    )

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_editable = ('order',)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order')
    list_editable = ('order',)
''')

write('apps/core/context_processors.py', '''
from .models import SiteSettings

def site_settings(request):
    try:
        site = SiteSettings.objects.first() or SiteSettings.objects.create()
    except:
        site = None
    return {'site_settings': site}
''')

write('apps/core/apps.py', '''
from django.apps import AppConfig
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
''')

# ====== COURSES APP ======
print("  ✓ apps/core")

write('apps/courses/models.py', '''
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Course Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=500)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/')
    duration = models.CharField(max_length=100, blank=True)
    eligibility = models.TextField(blank=True)
    features = RichTextField(blank=True)
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
''')

write('apps/courses/views.py', '''
from django.views.generic import ListView, DetailView
from .models import Course, CourseCategory

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 12

    def get_queryset(self):
        queryset = Course.objects.filter(is_published=True)
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_field = 'slug'
''')

write('apps/courses/urls.py', '''
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='detail'),
]
''')

write('apps/courses/admin.py', '''
from django.contrib import admin
from .models import CourseCategory, Course

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'order')
    list_filter = ('category', 'is_published')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
''')

write('apps/courses/apps.py', '''
from django.apps import AppConfig
class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.courses'
''')

print("  ✓ apps/courses")

# ====== BRANCHES APP ======
write('apps/branches/models.py', '''
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Branch(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='branches/')
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.city}"
''')

write('apps/branches/views.py', '''
from django.views.generic import ListView, DetailView
from .models import Branch

class BranchListView(ListView):
    model = Branch
    template_name = 'branches/branch_list.html'
    context_object_name = 'branches'

class BranchDetailView(DetailView):
    model = Branch
    template_name = 'branches/branch_detail.html'
    context_object_name = 'branch'
    slug_field = 'slug'
''')

write('apps/branches/urls.py', '''
from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [
    path('', views.BranchListView.as_view(), name='list'),
    path('<slug:slug>/', views.BranchDetailView.as_view(), name='detail'),
]
''')

write('apps/branches/admin.py', '''
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_active', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
''')

write('apps/branches/apps.py', '''
from django.apps import AppConfig
class BranchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.branches'
''')

print("  ✓ apps/branches")

# Create placeholder files for remaining apps
print("  ✓ apps/facilities")
write('apps/facilities/models.py', '''
from django.db import models
from ckeditor.fields import RichTextField

class Facility(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='facilities/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
''')
write('apps/facilities/views.py', 'from django.views.generic import ListView\nfrom .models import Facility\n\nclass FacilityListView(ListView):\n    model = Facility\n    template_name = "facilities/facility_list.html"\n    context_object_name = "facilities"')
write('apps/facilities/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "facilities"\n\nurlpatterns = [\n    path("", views.FacilityListView.as_view(), name="list"),\n]')
write('apps/facilities/admin.py', 'from django.contrib import admin\nfrom .models import Facility\n\n@admin.register(Facility)\nclass FacilityAdmin(admin.ModelAdmin):\n    list_display = ("name", "order")\n    list_editable = ("order",)')
write('apps/facilities/apps.py', 'from django.apps import AppConfig\nclass FacilitiesConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.facilities"')

print("  ✓ apps/gallery")
write('apps/gallery/models.py', '''
from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Gallery Categories'

    def __str__(self):
        return self.name

class GalleryItem(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
''')
write('apps/gallery/views.py', 'from django.views.generic import ListView\nfrom .models import GalleryItem\n\nclass GalleryListView(ListView):\n    model = GalleryItem\n    template_name = "gallery/gallery_list.html"\n    context_object_name = "items"')
write('apps/gallery/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "gallery"\n\nurlpatterns = [\n    path("", views.GalleryListView.as_view(), name="list"),\n]')
write('apps/gallery/admin.py', 'from django.contrib import admin\nfrom .models import GalleryCategory, GalleryItem\n\nadmin.site.register(GalleryCategory)\n\n@admin.register(GalleryItem)\nclass GalleryItemAdmin(admin.ModelAdmin):\n    list_display = ("title", "category", "order")\n    list_editable = ("order",)')
write('apps/gallery/apps.py', 'from django.apps import AppConfig\nclass GalleryConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.gallery"')

print("  ✓ apps/testimonials")
write('apps/testimonials/models.py', '''
from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
''')
write('apps/testimonials/views.py', 'from django.views.generic import ListView\nfrom .models import Testimonial\n\nclass TestimonialListView(ListView):\n    model = Testimonial\n    template_name = "testimonials/testimonial_list.html"\n    context_object_name = "testimonials"\n    queryset = Testimonial.objects.filter(is_active=True)')
write('apps/testimonials/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "testimonials"\n\nurlpatterns = [\n    path("", views.TestimonialListView.as_view(), name="list"),\n]')
write('apps/testimonials/admin.py', 'from django.contrib import admin\nfrom .models import Testimonial\n\n@admin.register(Testimonial)\nclass TestimonialAdmin(admin.ModelAdmin):\n    list_display = ("name", "title", "rating", "is_active", "order")\n    list_filter = ("is_active", "rating")\n    list_editable = ("order",)')
write('apps/testimonials/apps.py', 'from django.apps import AppConfig\nclass TestimonialsConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.testimonials"')

print("  ✓ apps/blog")
write('apps/blog/models.py', '''
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.CharField(max_length=500)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/')
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
''')
write('apps/blog/views.py', '''
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogCategory

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
''')
write('apps/blog/urls.py', '''
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='detail'),
]
''')
write('apps/blog/admin.py', '''
from django.contrib import admin
from .models import BlogCategory, BlogPost

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'featured', 'created_at')
    list_filter = ('category', 'is_published', 'featured')
    prepopulated_fields = {'slug': ('title',)}
''')
write('apps/blog/apps.py', 'from django.apps import AppConfig\nclass BlogConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.blog"')

print("  ✓ apps/admissions")
write('apps/admissions/models.py', '''
from django.db import models

class AdmissionEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Admission Enquiries'

    def __str__(self):
        return self.name
''')
write('apps/admissions/views.py', 'from django.shortcuts import render\nfrom django.views.generic import TemplateView\n\nclass AdmissionPageView(TemplateView):\n    template_name = "admissions/admission.html"')
write('apps/admissions/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "admissions"\n\nurlpatterns = [\n    path("", views.AdmissionPageView.as_view(), name="list"),\n]')
write('apps/admissions/admin.py', 'from django.contrib import admin\nfrom .models import AdmissionEnquiry\n\n@admin.register(AdmissionEnquiry)\nclass AdmissionEnquiryAdmin(admin.ModelAdmin):\n    list_display = ("name", "email", "course", "created_at", "is_read")\n    list_filter = ("is_read", "created_at")')
write('apps/admissions/apps.py', 'from django.apps import AppConfig\nclass AdmissionsConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.admissions"')

print("  ✓ apps/contact")
write('apps/contact/models.py', '''
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
''')
write('apps/contact/views.py', 'from django.shortcuts import render\nfrom django.views.generic import TemplateView\n\nclass ContactPageView(TemplateView):\n    template_name = "contact/contact.html"')
write('apps/contact/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "contact"\n\nurlpatterns = [\n    path("", views.ContactPageView.as_view(), name="list"),\n]')
write('apps/contact/admin.py', 'from django.contrib import admin\nfrom .models import ContactMessage\n\n@admin.register(ContactMessage)\nclass ContactMessageAdmin(admin.ModelAdmin):\n    list_display = ("name", "email", "subject", "created_at", "is_read")\n    list_filter = ("is_read", "created_at")')
write('apps/contact/apps.py', 'from django.apps import AppConfig\nclass ContactConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.contact"')

print("  ✓ apps/careers")
write('apps/careers/models.py', '''
from django.db import models

class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"
''')
write('apps/careers/views.py', 'from django.views.generic import ListView, DetailView\nfrom .models import JobOpening\n\nclass CareersView(ListView):\n    model = JobOpening\n    template_name = "careers/careers.html"\n    context_object_name = "jobs"\n    queryset = JobOpening.objects.filter(is_active=True)')
write('apps/careers/urls.py', 'from django.urls import path\nfrom . import views\n\napp_name = "careers"\n\nurlpatterns = [\n    path("", views.CareersView.as_view(), name="list"),\n]')
write('apps/careers/admin.py', 'from django.contrib import admin\nfrom .models import JobOpening, JobApplication\n\nadmin.site.register(JobOpening)\nadmin.site.register(JobApplication)')
write('apps/careers/apps.py', 'from django.apps import AppConfig\nclass CareersConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.careers"')

print("  ✓ apps/seo")
write('apps/seo/models.py', 'from django.db import models\n\nclass SEOPage(models.Model):\n    page_name = models.CharField(max_length=255)\n    meta_title = models.CharField(max_length=255)\n    meta_description = models.CharField(max_length=160)\n    meta_keywords = models.CharField(max_length=255, blank=True)\n\n    def __str__(self):\n        return self.page_name')
write('apps/seo/views.py', 'from django.shortcuts import render\n\ndef index(request):\n    return render(request, "core/index.html")')
write('apps/seo/urls.py', 'from django.urls import path\n\napp_name = "seo"')
write('apps/seo/admin.py', 'from django.contrib import admin\nfrom .models import SEOPage\n\nadmin.site.register(SEOPage)')
write('apps/seo/apps.py', 'from django.apps import AppConfig\nclass SeoConfig(AppConfig):\n    default_auto_field = "django.db.models.BigAutoField"\n    name = "apps.seo"')

# .GITIGNORE
print("\n📄 Creating .gitignore...")
write('.gitignore', '''
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
.DS_Store
''')

print("\n" + "═" * 80)
print("✅ PHASE 1 & 2 COMPLETE - Core Project Generated!")
print("═" * 80)

print("\n🎯 NEXT STEPS:\n")
print("1️⃣  Navigate to project:")
print("   cd 'c:\\\\Users\\\\dell\\\\Desktop\\\\evern website'\n")

print("2️⃣  Create virtual environment:")
print("   python -m venv venv")
print("   venv\\\\Scripts\\\\activate\n")

print("3️⃣  Install dependencies:")
print("   pip install -r requirements.txt\n")

print("4️⃣  Run migrations:")
print("   python manage.py makemigrations")
print("   python manage.py migrate\n")

print("5️⃣  Create superuser:")
print("   python manage.py createsuperuser\n")

print("6️⃣  Run development server:")
print("   python manage.py runserver\n")

print("7️⃣  Access the site:")
print("   http://localhost:8000/")
print("   Admin: http://localhost:8000/admin\n")

print("📝 To generate templates, run: python BUILD_TEMPLATES.py")
print("═" * 80)
