from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField('Slug', unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Категория документов'
        verbose_name_plural = 'Категории документов'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # преобразует в латиницу
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    file = models.FileField('Файл', upload_to='documents/')
    file_size = models.PositiveIntegerField('Размер файла', editable=False, default=0)
    downloads = models.PositiveIntegerField('Скачивания', default=0)
    order = models.PositiveIntegerField('Порядок', default=0)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
