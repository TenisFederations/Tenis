# core/models.py
from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название партнера")
    logo = models.ImageField(upload_to='partners/', verbose_name="Логотип")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка на сайт")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = ['name']  # можно сортировать по имени

    def __str__(self):
        return self.name
