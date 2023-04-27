import csv

from django.core.management.base import BaseCommand

from reviews.models import Title, Category, Genre, Comment, Review
from users.models import User


class Command(BaseCommand):
    help = 'load data from csv'

    def handle(self, *args, **options):
        with open('static/data/category.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                slug = row['slug']
                staff = Category(id=id, name=name, slug=slug)
                staff.save()
        csv_file.close()
        print('Категории загружены.')
        with open('static/data/titles.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                year = row['year']
                category = Category.objects.get(id=int(row['category']))
                staff = Title(id=id, name=name, year=year, category=category)
                staff.save()
        csv_file.close()
        print('Произведения загружены.')
        with open('static/data/genre.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                name = row['name']
                slug = row['slug']
                staff = Genre(id=id, name=name, slug=slug)
                staff.save()
        csv_file.close()
        print('Жанры загружены.')
        with open('static/data/genre_title.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                title = Title.objects.get(id=row['title_id'])
                genre = Genre.objects.get(id=row['genre_id'])
                title.genre.add(genre)
                title.save()
        csv_file.close()
        print('Cвязи категории и жанров загружены.')
        with open('static/data/users.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                username = row['username']
                email = row['email']
                role = row['role']
                staff = User(id=id, username=username, email=email, role=role)
                staff.save()
        csv_file.close()
        print('Юзеры загружены.')
        with open('static/data/review.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                title_id = row['title_id']
                text = row['text']
                author = User.objects.get(id=row['author'])
                pub_date = row['pub_date']
                score = row['score']
                staff = Review(id=id, title_id=title_id, text=text,
                               author=author, pub_date=pub_date, score=score)
                staff.save()
        csv_file.close()
        print('Отзывы загружены.')
        with open('static/data/comments.csv', encoding='utf8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                id = row['id']
                review_id = row['review_id']
                text = row['text']
                author = User.objects.get(id=row['author'])
                pub_date = row['pub_date']
                staff = Comment(id=id, review_id=review_id,
                                text=text, author=author, pub_date=pub_date)
                staff.save()
        csv_file.close()
        print('Комментарии загружены.')
