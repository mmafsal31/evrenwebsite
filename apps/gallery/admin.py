from django.contrib import admin
from .models import GalleryCategory, GalleryItem

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category",)
    list_editable = ("order",)
    search_fields = ("title", "category__name")
