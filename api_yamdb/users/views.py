from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import User
from .srializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination


def get_some():
    pass
