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
