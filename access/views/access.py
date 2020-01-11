"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)


from access.serializers import (
    UserModelSerializer,
    LoginSerializer,
)

from administration.models import User


class AccessViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_voting_chief=True, is_active=True)
    serializer_class = LoginSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [AllowAny]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        Public login for admin users.

        Users could be:

        - Staff: User with privileges to create polls, users and check statistics.
        - Voting chief: User with privileges to asign current polls to voters.
        - Voting node: User used by voters to fill a poll

        :return: a view instance
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
