"""Rides views."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

from access.permissions import IsVoterNode
from publicpoll.serializers import PollModelSerializer, AnswerModelSerializer
from access.serializers import VoterModelSerializer, ConsultTokenSerializer
from access.models import ConsultModel

from django.utils import timezone

class PollConsultViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """

    list:
        Voter set his token, and will receive the poll with the questions to answer.

    """

    lookup_field = 'token'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ConsultTokenSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated, IsVoterNode]
        return [p() for p in permissions]

    def get_queryset(self):
        """Get available tokens"""
        return ConsultModel.objects.filter(expiration__gte = timezone.now(), answered = False).exclude(token__exact='')

    def retrieve(self, request, *args, **kwargs):
        """
        Obtain poll of the existing token.
        """
        response = super(PollConsultViewSet, self).retrieve(request, *args, **kwargs)
        consult = self.get_object()
        print(consult)
        data = {
            'voter': VoterModelSerializer(consult.voter, many=False).data,
            'poll': PollModelSerializer(consult.poll, many=False).data,
            'expiry': consult.expiration,
        }
        response.data = data
        return response

    @action(detail=True, methods=['post'])
    def answer(self, request, *args, **kwargs):
        """
        Generate token to user to answer the poll.
        """
        consult = self.get_object()
        serializer = AnswerModelSerializer(
            data=request.data,
            context={'poll': consult.poll, 'consult':consult}
        )
        serializer.is_valid(raise_exception=True)
        status_load = serializer.save()
        data = {
            'status' : status_load
        }
        return Response(data, status=status.HTTP_201_CREATED)
