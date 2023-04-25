from django.core.management.base import BaseCommand
import csv
from reviews.models import Title, Category, Genre, TitleGenre


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
                staff = TitleGenre(id=id, title=title, genre=genre)
                staff.save()
        csv_file.close()
        print('Cвязи категории и жанров загружены.')
