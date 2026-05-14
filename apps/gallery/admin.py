from django.contrib import admin
from .models import GalleryCategory, GalleryItem

admin.site.register(GalleryCategory)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_editable = ("order",)