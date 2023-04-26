from reviews.models import Genre, Title, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, required=False)
    category = CategorySerializer(many=False, required=False)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


