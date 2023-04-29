from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .pagination import CustomPagination
from .permissions import AdminAndSuperUser
from .registration.confirm_code_generator import generator
from .registration.send_code_to_email import send_confirm_code_to_email
from .registration.token_generator import get_tokens_for_user
from .serializers import (GetTokenSerializer, SignUpSerializer,
                          UserProfileSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminAndSuperUser,)
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = "username"
    http_method_names = ['get', 'post', 'patch', 'delete']

    def create(self, request, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            if User.objects.filter(email=email).first():
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            user, created = User.objects.get_or_create(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        email = serializer.data['email']

        user, created = User.objects.get_or_create(
            username=username,
            email=email
        )
        user.confirmation_code = generator()
        user.save()
        send_confirm_code_to_email(user, email)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.data['username']
        code = serializer.data['confirmation_code']
        if User.objects.filter(username=username).first():
            user = User.objects.get(username=username)
            if user.confirmation_code == code:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated])
def me(request):
    if request.method == "GET":
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PATCH":
        serializer = UserProfileSerializer(
            request.user, partial=True, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
