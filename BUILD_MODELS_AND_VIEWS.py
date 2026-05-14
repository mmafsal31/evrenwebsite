#!/usr/bin/env python3
"""
EVREN ACADEMY - MODELS & VIEWS GENERATOR (Phase 2)
This script creates all Django models, views, URLs, forms, and admin configurations
Run AFTER: python BUILD_PROJECT.py && pip install -r requirements.txt
Run: python BUILD_MODELS_AND_VIEWS.py
"""

from pathlib import Path
from textwrap import dedent

BASE = Path(__file__).parent

def write_file(rel_path, content):
    path = BASE / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content), encoding='utf-8')
    print(f"  ✓ {rel_path}")

print("╔" + "═" * 70 + "╗")
print("║" + " PHASE 2: MODELS & VIEWS GENERATION ".center(70) + "║")
print("╚" + "═" * 70 + "╝\n")

# =========================================================================
# CORE APP - MODELS
# =========================================================================
print("📦 Creating CORE app models...")

write_file('apps/core/models.py', """
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default='Evren Academy')
    site_url = models.URLField(default='http://localhost:8000')
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='media/', blank=True, null=True)
    favicon = models.ImageField(upload_to='media/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, default='+92 (0) 123 456 789')
    whatsapp_number = models.CharField(max_length=20, default='+92 300 1234567')
    email = models.EmailField(default='info@everenacademy.com')
    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Social media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    # Colors
    primary_color = models.CharField(max_length=7, default='#0B5D3B')
    secondary_color = models.CharField(max_length=7, default='#D4AF37')
    accent_color = models.CharField(max_length=7, default='#F8F5EE')
    
    # Footer
    footer_text = models.TextField(blank=True)
    copyright = models.CharField(max_length=255, default='© 2024 Evren Academy. All rights reserved.')
    
    # Announcement
    announcement_text = models.CharField(max_length=500, blank=True)
    show_announcement = models.BooleanField(default=False)
    
    # Google Map
    google_map_embed = models.TextField(blank=True)
    google_maps_api_key = models.CharField(max_length=255, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Site Settings'
    
    def __str__(self):
        return self.site_name

class HeroSlide(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=100, blank=True, default='Learn More')
    button_link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    
    class Meta:
        verbose_name_plural = 'About Sections'
    
    def __str__(self):
        return self.title

class Statistic(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True)
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.label} ({self.value})"

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class SEOModel(models.Model):
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    og_title = models.CharField(max_length=255, blank=True)
    og_description = models.CharField(max_length=255, blank=True)
    og_image = models.ImageField(upload_to='og/', blank=True, null=True)
    
    class Meta:
        abstract = True
""")

# =========================================================================
# CORE APP - VIEWS
# =========================================================================
print("📝 Creating CORE app views...")

write_file('apps/core/views.py', """
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

class AboutPageView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = get_site_settings()
        context['team_members'] = TeamMember.objects.all()
        return context

def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)

def server_error(request):
    return render(request, 'errors/500.html', status=500)

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def terms_conditions(request):
    return render(request, 'pages/terms.html')
""")

# =========================================================================
# CORE APP - URLs
# =========================================================================
print("📝 Creating CORE app URLs...")

write_file('apps/core/urls.py', """
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy'),
    path('terms/', views.terms_conditions, name='terms'),
]
""")

# =========================================================================
# CORE APP - ADMIN
# =========================================================================
print("📝 Creating CORE app admin...")

write_file('apps/core/admin.py', """
from django.contrib import admin
from .models import SiteSettings, HeroSlide, AboutSection, Statistic, TeamMember

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {'fields': ('site_name', 'site_url', 'tagline', 'description')}),
        ('Media', {'fields': ('logo', 'favicon')}),
        ('Contact Information', {'fields': ('phone_number', 'whatsapp_number', 'email', 'address', 'latitude', 'longitude')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'youtube_url')}),
        ('Colors', {'fields': ('primary_color', 'secondary_color', 'accent_color')}),
        ('Footer & Announcement', {'fields': ('footer_text', 'copyright', 'announcement_text', 'show_announcement')}),
        ('Google Maps', {'fields': ('google_map_embed', 'google_maps_api_key')}),
    )

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('order',)
    ordering = ('order',)

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'unit', 'order')
    list_editable = ('order',)
    ordering = ('order',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'order')
    list_editable = ('order',)
    ordering = ('order',)
""")

# =========================================================================
# CORE APP - Context Processor
# =========================================================================
print("📝 Creating CORE context processor...")

write_file('apps/core/context_processors.py', """
from .models import SiteSettings

def site_settings(request):
    try:
        site = SiteSettings.objects.first() or SiteSettings.objects.create()
    except:
        site = None
    
    return {
        'site_settings': site,
    }
""")

write_file('apps/core/__init__.py', '')
write_file('apps/core/apps.py', '''
from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    verbose_name = 'Core'
''')

# =========================================================================
# COURSES APP
# =========================================================================
print("📦 Creating COURSES app...")

write_file('apps/courses/models.py', """
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from apps.core.models import SEOModel

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name_plural = 'Course Categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Course(SEOModel):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=500)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/')
    duration = models.CharField(max_length=100, blank=True)
    eligibility = models.TextField(blank=True)
    features = RichTextField(blank=True)
    curriculum = RichTextField(blank=True)
    fee = models.CharField(max_length=100, blank=True)
    intake_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.meta_title:
            self.meta_title = self.name
        if not self.meta_description:
            self.meta_description = self.short_description[:160]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Curriculum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='curriculum_items')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
""")

write_file('apps/courses/views.py', """
from django.shortcuts import render, get_object_or_404
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
        context['selected_category'] = self.request.GET.get('category', '')
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_courses'] = Course.objects.filter(
            category=self.object.category,
            is_published=True
        ).exclude(id=self.object.id)[:4]
        return context
""")

write_file('apps/courses/urls.py', """
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='detail'),
]
""")

write_file('apps/courses/admin.py', """
from django.contrib import admin
from .models import CourseCategory, Course, Curriculum

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CurriculumInline(admin.TabularInline):
    model = Curriculum
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published', 'featured', 'order')
    list_filter = ('category', 'is_published', 'featured')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CurriculumInline]
    fieldsets = (
        ('Basic Information', {'fields': ('name', 'slug', 'category', 'short_description', 'image')}),
        ('Details', {'fields': ('description', 'duration', 'eligibility', 'fee', 'intake_date')}),
        ('Content', {'fields': ('features', 'curriculum')}),
        ('Publishing', {'fields': ('is_published', 'featured', 'order')}),
        ('SEO', {'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
    )
""")

write_file('apps/courses/__init__.py', '')
write_file('apps/courses/apps.py', '''
from django.apps import AppConfig
class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.courses'
''')

# =========================================================================
# BRANCHES APP
# =========================================================================
print("📦 Creating BRANCHES app...")

write_file('apps/branches/models.py', """
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from apps.core.models import SEOModel

class Branch(SEOModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='branches/')
    description = RichTextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
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
""")

write_file('apps/branches/views.py', """
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
""")

write_file('apps/branches/urls.py', """
from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [
    path('', views.BranchListView.as_view(), name='list'),
    path('<slug:slug>/', views.BranchDetailView.as_view(), name='detail'),
]
""")

write_file('apps/branches/admin.py', """
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_active', 'order')
    list_filter = ('city', 'is_active')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
""")

write_file('apps/branches/__init__.py', '')
write_file('apps/branches/apps.py', '''
from django.apps import AppConfig
class BranchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.branches'
''')

print("\n✅ Phase 2 COMPLETE: Models & Views generated!")
print("\nNext steps:")
print("  1. Run: python manage.py makemigrations")
print("  2. Run: python manage.py migrate")
print("  3. Run: python manage.py createsuperuser")
print("  4. Run: python BUILD_TEMPLATES.py")
