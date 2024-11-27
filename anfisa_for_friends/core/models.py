from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
