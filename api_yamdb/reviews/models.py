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
        through='TitleGenre'
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


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        #  после создания базы раскоментить
        #auto_created = True
        verbose_name = 'Произведение+жанр'
        verbose_name_plural = 'Произведения+жанры'
        constraints = (
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name='one title = one genre'
            ),
        )

    def __str__(self):
        return (f'Связь {self.title}, {self.genre} разорвана будет разорвана.')
=======


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
        help_text='Автор отзыва'
    )
    composition = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Произведение на которое написан отзыв'
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Введи текст отзыва'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации отзыва',
        help_text='Дата публикации отзыва'
    )
    score = models.IntegerField(
        verbose_name='Оценка произведению',
        help_text='Введите оценку произведению',
        # Оценка может быть целым числом от 1 до 10
        validators=[
            MinValueValidator(1),
            MinValueValidator(10)
        ],
    )

    class Meta:
        """Делаем ограничение на количество ревью одним автором."""
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'composition'],
                name='one author = one review per composition'
            ),
        )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор комментария'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        help_text='Комментируемый отзыв'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации комментария',
        help_text='Дата публикации комментария'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text
