from django.db import models

class Subdivision(models.Model):
    SUBDIVISION_CHOICES = [
        ('members', 'Члены федерации'),
        ('general_meeting', 'Общее собрание'),
        ('board', 'Правление'),
        ('chairman', 'Председатель'),
        ('vice_chairman', 'Заместители председателя'),
        ('secretary', 'Ответственный секретарь'),
        ('coaches_council', 'Тренерский совет'),
        ('audit_committee', 'Контрольно-счетная комиссия'),
        ('judges_committee', 'Судейская дисциплинарная комиссия'),
    ]
    
    title = models.CharField(max_length=50, choices=SUBDIVISION_CHOICES, unique=True, verbose_name='Подразделение')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.get_title_display()


class Person(models.Model):
    subdivisions = models.ManyToManyField(Subdivision, related_name='members', verbose_name='Подразделения')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    role = models.CharField(max_length=150, blank=True, verbose_name='Должность')
    photo = models.ImageField(upload_to='persons_photos/', blank=True, null=True, verbose_name='Фото')
    email = models.EmailField(blank=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=30, blank=True, verbose_name='Телефон')
    bio = models.TextField(blank=True, verbose_name='О сотруднике')
    period = models.CharField(max_length=100, blank=True, verbose_name='Стаж работы')
    sort_order = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        ordering = ['sort_order']
        verbose_name = "Член подраздела"
        verbose_name_plural = "Члены подразделов"

    def __str__(self):
        return self.full_name
