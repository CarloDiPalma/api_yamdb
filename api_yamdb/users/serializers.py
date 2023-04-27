from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(
        read_only=True
    )
    role = serializers.ReadOnlyField()

    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        model = User
        read_only_fields = ('username', 'role')


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True
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
