from django.contrib import admin
from .models import SEOPage

@admin.register(SEOPage)
class SEOPageAdmin(admin.ModelAdmin):
    list_display = ("page_name", "meta_title")
    search_fields = ("page_name", "meta_title", "meta_description", "meta_keywords")
