from django.contrib import admin
from .models import JobOpening, JobApplication

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "deadline", "is_active", "created_at")
    list_filter = ("is_active", "location", "deadline")
    search_fields = ("title", "description", "location")
    list_editable = ("is_active",)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "email", "phone", "created_at")
    list_filter = ("job", "created_at")
    search_fields = ("name", "email", "phone", "job__title")
