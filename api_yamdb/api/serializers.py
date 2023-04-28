from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from reviews.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, )
    category = CategorySerializer(many=False, required=False)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    score = serializers.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        )
    )

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'score', 'pub_date')

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        user = self.context['request'].user
        if Review.objects.filter(title=title, author=user).exists():
            raise serializers.ValidationError(
                'Можно сделать только один отзыв на произведение'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
