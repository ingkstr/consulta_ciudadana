"""Voter check data and pending poll views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import (
    IsAuthenticated,
)


from access.serializers import (
    VoterModelSerializer,
    PollBriefModelSerializer,
    ConsultModelSerializer
)

from access.permissions import IsVoterChief

from administration.models import Voter, Poll
from access.models import ConsultModel


class VoterCheckViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """Chief actions"""

    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return PollBriefModelSerializer
        return ConsultModelSerializer

    def get_queryset(self):
        """Get available polls of voter"""
        now = timezone.now()
        answered_polls = ConsultModel.objects.filter(voter = self.voter, poll__start_datetime__lte = now, poll__end_datetime__gte = now, poll__ready = True).values_list('poll__pk',)
        #answered_polls =  self.voter.polls.filter(start_datetime__lte = now, end_datetime__gte = now, ready = True).values_list('pk',)
        return Poll.objects.filter(start_datetime__lte = now, end_datetime__gte = now, ready = True).exclude(id__in= answered_polls)

    def dispatch(self, request, *args, **kwargs):
        """Verify that the voter exists."""
        cid = kwargs['cid']
        self.voter = get_object_or_404(Voter, cid=cid,alive=True)
        return super(VoterCheckViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated, IsVoterChief]
        return [p() for p in permissions]

    def list(self, request, *args, **kwargs):
        """Add extra data to the response."""
        response = super(VoterCheckViewSet, self).list(request, *args, **kwargs)
        data = {
            'voter': VoterModelSerializer(self.voter, many=False).data,
            'available_polls': PollBriefModelSerializer(self.get_queryset(), many=True).data,
        }
        response.data = data
        return response

    @action(detail=True, methods=['post'])
    def assign(self, request, *args, **kwargs):
        """Generate token to user to answer the poll"""
        poll = self.get_object()
        voter = self.voter
        serializer = ConsultModelSerializer(
            data=request.data,
            context={'voter': voter, 'poll': poll}
        )
        serializer.is_valid(raise_exception=True)
        token, expiration = serializer.save()
        data = {
            'voter': VoterModelSerializer(voter, many=False).data,
            'poll' : PollBriefModelSerializer(poll, many=False).data,
            'expiration': expiration,
            'token' : token
        }
        return Response(data, status=status.HTTP_201_CREATED)
