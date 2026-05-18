
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
    LEVEL_CHOICES = (
        ('foundation', 'Foundation'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('all_levels', 'All Levels'),
    )

    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=500)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/')
    hero_image = models.ImageField(upload_to='courses/hero/', blank=True, null=True)
    overview = RichTextField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES, blank=True)
    fees = models.CharField(max_length=100, blank=True)
    eligibility = models.TextField(blank=True)
    features = RichTextField(blank=True)
    curriculum = RichTextField(blank=True)
    faqs = RichTextField(blank=True, help_text='Add FAQs as headings and paragraphs or as a list.')
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

    @property
    def display_hero_image(self):
        return self.hero_image or self.image

    @property
    def display_overview(self):
        return self.overview or self.description
