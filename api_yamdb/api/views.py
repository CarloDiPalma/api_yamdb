from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django_filters.rest_framework import (CharFilter, DjangoFilterBackend,
                                           FilterSet)
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Comment, Genre, Review, Title

from .permissions import AdminOrReadOnly, AuthorAdminModeratorOrReadOnly, \
    CommentPermissions
from .serializers import (CategorySerializer, CommentSerializer,
                          CreateTitleSerializer, GenreSerializer,
                          ReviewSerializer, TitleSerializer)


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
    queryset = Title.objects.annotate(rating=Avg("reviews__score"))
    permission_classes = (AdminOrReadOnly,)
    serializer_class = TitleSerializer
    create_serializer_class = CreateTitleSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return self.create_serializer_class
        return self.serializer_class


class CategoryViewSet(CreateListViewSet):
    queryset = Category.objects.all()
    permission_classes = (AdminOrReadOnly,)
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateListViewSet):
    queryset = Genre.objects.all()
    permission_classes = (AdminOrReadOnly,)
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
            Title,
            pk=self.kwargs.get('title_id')
        ).reviews.select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            **{'title': get_object_or_404(
                Title, pk=self.kwargs.get('title_id')
            )
            }
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CommentPermissions,)

    def get_queryset(self):
        return get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id')
        ).comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            **{'review': get_object_or_404(
                Review,
                pk=self.kwargs.get('review_id')
            )
            }
        )
