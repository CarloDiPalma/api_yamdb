# Generated by Django 3.2 on 2023-04-28 04:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Здесь нужно ввести название категории.', max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Здесь нужно задать слаг категории.', unique=True, verbose_name='Слаг категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите текст комментария', verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Дата публикации комментария', verbose_name='Дата публикации комментария')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Здесь нужно ввести название жанра.', max_length=100, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Здесь нужно задать слаг жанра.', unique=True, verbose_name='Слаг жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введи текст отзыва', verbose_name='Текст отзыва')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Дата публикации отзыва', verbose_name='Дата публикации отзыва')),
                ('score', models.IntegerField(help_text='Введите оценку произведению', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка произведению')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Здесь нужно ввести название произведения.', max_length=200, verbose_name='Название произведения')),
                ('year', models.PositiveIntegerField(default=2023, help_text='Здесь нужно ввести год выхода.', validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2023)], verbose_name='Год выхода')),
                ('description', models.TextField(blank=True, help_text='Здесь нужно ввести описание.', verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, help_text='Здесь нужно выбрать категорию.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(blank=True, help_text='Здесь нужно выбрать жанр. Чтобы выбрать несколько удерживайте Ctrl (Win), или Cmd (Mac)', related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
            },
        ),
    ]
