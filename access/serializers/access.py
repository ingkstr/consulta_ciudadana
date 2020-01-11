"""Users serializers."""

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from administration.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    class Meta:
        """Meta class."""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class LoginSerializer(serializers.Serializer):
    """Chief login serializer. """

    username = serializers.CharField(max_length=25)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_voting_chief and not user.is_voting_node:
            raise serializers.ValidationError('Account is not voting chief or voting node.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
