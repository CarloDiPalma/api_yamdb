# Generated by Django 3.2 on 2023-04-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, help_text='Здесь нужно выбрать жанр.', to='reviews.Genre', verbose_name='Жанр'),
        ),
    ]
