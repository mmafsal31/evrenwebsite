
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
