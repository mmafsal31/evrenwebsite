
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus_type', 'city', 'is_active', 'order')
    list_filter = ('campus_type', 'is_active')
    list_editable = ('is_active', 'order')
    search_fields = ('name', 'city', 'address', 'phone', 'email', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Campus Details', {
            'fields': ('name', 'slug', 'campus_type', 'city', 'address', 'phone', 'email', 'image')
        }),
        ('Page Content', {
            'fields': ('description', 'infrastructure_details', 'facilities_available')
        }),
        ('Display Controls', {
            'fields': ('is_active', 'order')
        }),
    )
