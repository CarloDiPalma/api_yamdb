from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .generators.confirm_code_generator import generator
from .models import User
from .serializers import UserSerializer, SignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination


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
        send_mail(
            'Confirmation code for registration on Yamdb',
            user.confirmation_code,
            'from@example.com',
            [email],
            fail_silently=False
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
