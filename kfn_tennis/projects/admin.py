from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectCategory


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'status',
        'is_active',
        'start_date',
        'image_preview',
    )

    list_filter = ('category', 'status', 'is_active')
    search_fields = ('title', 'short_description', 'full_description')
    list_editable = ('status', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', '-start_date')

    readonly_fields = (
        'image_preview',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'title',
                'slug',
                'category',
                'status',
                'is_active',
                'order',
            )
        }),
        ('Описание проекта', {
            'fields': (
                'short_description',
                'full_description',
            )
        }),
        ('Визуальные материалы', {
            'fields': (
                'main_image',
                'image_preview',
            )
        }),
        ('Ключевая информация', {
            'fields': (
                ('start_date', 'end_date'),
                'location',
                'prize_fund',
            )
        }),
        ('Ссылки и документы', {
            'fields': (
                'attachment',
                'external_link',
                'gallery_link',
            )
        }),
        ('Контакты', {
            'fields': ('contacts',)
        }),
        ('Системная информация', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    def image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="max-height:120px;border-radius:6px;" />',
                obj.main_image.url
            )
        return '—'

    image_preview.short_description = 'Превью'
