# core/admin.py
from django.contrib import admin
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
