from django.shortcuts import get_object_or_404

from django_filters.rest_framework import (CharFilter, DjangoFilterBackend,
                                           FilterSet)
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category, Genre, Title, Review, Comment

from .permissions import AuthorAdminModeratorOrReadOnly
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          ReviewSerializer,
                          CommentSerializer
                          )


class CreateListViewSet(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class TitleFilter(FilterSet):
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = ('name', 'year')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter


class CategoryViewSet(CreateListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateListViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorAdminModeratorOrReadOnly,)

    def get_queryset(self):
        return get_object_or_404(
            Review, pk=self.kwargs.get('title_id')
        ).reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            **{self.title: get_object_or_404(
                self.Title, pk=self.kwargs.get(self.title_id)
            )
            }
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorAdminModeratorOrReadOnly,)

    def get_queryset(self):
        return get_object_or_404(
            Comment,
            pk=self.kwargs.get('review_id')
        ).comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            **{self.review: get_object_or_404(
                self.Review,
                pk=self.kwargs.get(self.review_id)
            )
            }
        )
