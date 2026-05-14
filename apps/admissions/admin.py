from django.contrib import admin
from .models import AdmissionEnquiry

@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "course", "created_at", "is_read")
    list_filter = ("is_read", "created_at")