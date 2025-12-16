from django.contrib import admin
from .models import Category, Document

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file', 'file_size', 'downloads', 'created_at')
    list_filter = ('category', 'created_at', 'tags')
    search_fields = ('title', 'description')
    ordering = ('order', '-created_at')
    readonly_fields = ('file_size', 'downloads', 'created_at', 'updated_at')
