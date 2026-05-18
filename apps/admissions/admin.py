from django.contrib import admin
from .models import AdmissionEnquiry

@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_name", "phone", "email", "course", "campus_preference", "created_at", "is_read")
    list_filter = ("course", "campus_preference", "is_read", "created_at")
    search_fields = ("name", "parent_name", "phone", "email", "course")
    list_editable = ("is_read",)
