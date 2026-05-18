from django.contrib import admin
from .models import JobOpening, JobApplication

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "deadline", "is_active", "created_at")
    list_filter = ("is_active", "location", "deadline")
    search_fields = ("title", "description", "location")
    list_editable = ("is_active",)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Job Details", {
            "fields": ("title", "description", "location", "salary_range", "deadline")
        }),
        ("Publishing Controls", {
            "fields": ("is_active", "created_at")
        }),
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "email", "phone", "created_at")
    list_filter = ("job", "created_at")
    search_fields = ("name", "email", "phone", "job__title")
    readonly_fields = ("created_at",)
