from django.contrib import admin
from .models import Facility

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    search_fields = ("name", "description")
    fieldsets = (
        ("Facility Content", {
            "fields": ("name", "description", "image", "order")
        }),
    )
