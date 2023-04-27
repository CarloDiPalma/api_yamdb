from rest_framework import serializers
from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     super(TitleSerializer, self).__init__(*args, **kwargs)
    #     if 'view' in self.context and self.context['view'].action != 'create':
    #         self.fields.update({"genre": GenreSerializer(many=True, required=False)})
    #         self.fields.update({"category": CategorySerializer(many=False, required=False)})
    genre = GenreSerializer(many=True, )
    category = CategorySerializer(many=False, required=False)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title

    # def create(self, validated_data):
    #     genres = validated_data.pop('genre')
    #     category = validated_data.pop('category')
    #     title = Title.objects.create(**validated_data)
    #     for genre in genres:
    #         current_genre = Genre.objects.get(slug=genre)
    #         title.genre.add(current_genre)
    #         title.save()
    #     current_category = Category.objects.get(slug=category)
    #     title.category = current_category
    #     title.save()
    #     return title


