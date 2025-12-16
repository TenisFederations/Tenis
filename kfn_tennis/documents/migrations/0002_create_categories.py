from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('documents', 'Category')
    categories = [
        ('Нормативные документы', 1),
        ('Приказы', 2),
        ('Положения', 3),
        ('Программа развития', 4),
        ('Протоколы заседаний', 5),
        ('Антидопинговые материалы', 6),
        ('Статистические отчеты', 7),
    ]
    for name, order in categories:
        slug = name.lower().replace(' ', '-')
        if not Category.objects.filter(slug=slug).exists():
            Category.objects.create(name=name, order=order, slug=slug)

class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
