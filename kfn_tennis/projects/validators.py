import os
from django.core.exceptions import ValidationError


def validate_project_file(file):
    ext = os.path.splitext(file.name)[1].lower()
    allowed_extensions = ['.pdf', '.doc', '.docx']

    if ext not in allowed_extensions:
        raise ValidationError(
            'Допустимые форматы файлов: PDF, DOC, DOCX'
        )

    if file.size > 10 * 1024 * 1024:
        raise ValidationError(
            'Размер файла не должен превышать 10 МБ'
        )
