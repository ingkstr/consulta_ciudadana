from rest_framework import mixins, status, viewsets
from django.utils import timezone

from administration.models import Poll
from publicpoll.models import Statistics

from access.serializers import PollBriefModelSerializer, StatsModelSerializer

from publicpoll.serializers import PollModelSerializer


from rest_framework.permissions import (
    IsAuthenticated,
)

from access.permissions import IsStaff

class StatsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """

    get:
    Viewset to list stats of ended polls.

    """

    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return PollBriefModelSerializer
        if self.action == 'retrieve':
            return PollModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated, IsStaff]
        return [p() for p in permissions]

    def get_queryset(self):
        """Get ended ready polls"""
        now = timezone.now()
        return Poll.objects.filter(end_datetime__lte = now, ready = True)

    def retrieve(self, request, *args, **kwargs):
        """Add stats to retrieve data"""
        response = super(StatsViewSet, self).retrieve(request, *args, **kwargs)
        poll = self.get_object()
        stats = Statistics.objects.filter(poll = poll).order_by("question")
        data = {
            'poll': response.data,
            'stats': StatsModelSerializer(stats, many=True).data,
        }
        response.data = data
        return response
