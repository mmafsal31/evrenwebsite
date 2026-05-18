
from django.contrib import admin
from .models import CourseCategory, Course

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'featured', 'is_published', 'order')
    list_filter = ('category', 'featured', 'is_published')
    list_editable = ('featured', 'is_published', 'order')
    search_fields = ('name', 'short_description', 'description', 'eligibility')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Course Details', {
            'fields': ('category', 'name', 'slug', 'short_description', 'description', 'image')
        }),
        ('Program Information', {
            'fields': ('duration', 'eligibility', 'features')
        }),
        ('Publishing Controls', {
            'fields': ('featured', 'is_published', 'order', 'created_at')
        }),
    )
