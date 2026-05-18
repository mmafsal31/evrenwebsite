
from django.contrib import admin
from django.utils.html import format_html
from .models import CourseCategory, Course

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'duration', 'featured', 'is_published', 'order')
    list_filter = ('category', 'featured', 'is_published')
    list_editable = ('featured', 'is_published', 'order')
    search_fields = ('name', 'short_description', 'description', 'eligibility')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'image_preview', 'hero_image_preview')
    fieldsets = (
        ('Course Details', {
            'fields': ('category', 'name', 'slug', 'short_description', 'overview', 'description')
        }),
        ('Images', {
            'fields': ('image', 'image_preview', 'hero_image', 'hero_image_preview')
        }),
        ('Program Information', {
            'fields': ('duration', 'level', 'fees', 'eligibility', 'features', 'curriculum', 'faqs')
        }),
        ('Publishing Controls', {
            'fields': ('featured', 'is_published', 'order', 'created_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 220px; border-radius: 8px;" />', obj.image.url)
        return 'No image uploaded'

    def hero_image_preview(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-width: 260px; border-radius: 8px;" />', obj.hero_image.url)
        return 'No hero image uploaded'
