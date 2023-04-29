from django.contrib import admin

from .models import Category, Genre, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'get_genres', 'category')
    empty_value_display = '-пусто-'
    search_fields = ('name',)

    def get_genres(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])
    get_genres.short_description = 'Жанр'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
