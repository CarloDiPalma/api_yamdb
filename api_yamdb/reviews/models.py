from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Titles(models.Model):
    pass


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
    rating = models.IntegerField(
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
