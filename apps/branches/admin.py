
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus_type', 'city', 'is_active', 'order')
    list_filter = ('campus_type', 'is_active')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
