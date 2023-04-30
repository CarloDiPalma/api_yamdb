# api_yamdb
Проект группы 73

## Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха.

Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.

## Документация и эндпоинты

Список эндпоинтов и документация доступны по адресу: http://127.0.0.1:8000/redoc/

## Команда разработки
[Maksim-Good](https://github.com/Maksim-Good) - категории, жанры, импорт данных.
[dim3p](https://github.com/dim3p) - рейтинг произведений, отзывы, комментарии.
[CarloDiPalma](https://github.com/CarloDiPalma) - работа с токеном, регистрация, аутентификация, права доступа.

