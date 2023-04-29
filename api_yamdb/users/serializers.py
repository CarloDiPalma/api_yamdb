from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UnicodeUsernameValidator()],
    )
    email = serializers.EmailField(
        max_length=254
    )

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=150,
        required=True,
        validators=[UnicodeUsernameValidator()],
    )
    email = serializers.EmailField(
        max_length=254,
        required=True
    )

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if username == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не должно быть "me"'
            )

        if not User.objects.filter(
            username=username,
            email=email
        ).exists():
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError(
                    f'Имя {username} уже занято'
                )
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    f'Почта {email} уже занята'
                )
        return data

    class Meta:
        fields = (
            'username', 'email'
        )
        model = User


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=6,
        required=True
    )
