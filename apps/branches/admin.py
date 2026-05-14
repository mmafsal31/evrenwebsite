
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_active', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
