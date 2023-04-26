from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название жанра',
        help_text='Здесь нужно ввести название жанра.',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг жанра',
        help_text='Здесь нужно задать слаг жанра.',
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название произведения',
        help_text='Здесь нужно ввести название произведения.',
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выхода',
        help_text='Здесь нужно ввести год выхода.',
        # Год выхода с 1800 до сего года
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.now().year)],
        default=datetime.now().year,
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Здесь нужно ввести описание.',
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True,
        verbose_name='Жанр',
        help_text='Здесь нужно выбрать жанр. '
        'Чтобы выбрать несколько удерживайте Ctrl (Win), или Cmd (Mac)',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория',
        help_text='Здесь нужно выбрать категорию.',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name

    def get_rating(self):
        pass


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории',
        help_text='Здесь нужно ввести название категории.',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Слаг категории',
        help_text='Здесь нужно задать слаг категории.',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
