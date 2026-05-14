from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "rating", "is_active", "order")
    list_filter = ("is_active", "rating")
    list_editable = ("order",)