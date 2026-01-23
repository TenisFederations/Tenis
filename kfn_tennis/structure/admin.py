from django.contrib import admin
from .models import Subdivision, Person

class PersonInline(admin.TabularInline):
    model = Person.subdivisions.through
    extra = 1
    verbose_name = "Член подраздела"
    verbose_name_plural = "Члены подраздела"


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [PersonInline]
    search_fields = ['members__full_name']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'is_active', 'sort_order')
    list_filter = ('subdivisions', 'is_active')
    search_fields = ('full_name', 'email')
    ordering = ('sort_order',)


