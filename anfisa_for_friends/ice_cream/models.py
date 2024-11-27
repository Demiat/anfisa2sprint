from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        'Обертка',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
