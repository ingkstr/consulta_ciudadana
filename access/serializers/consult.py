from rest_framework import serializers

from access.models import ConsultModel
from administration.models import Voter,Poll

from django.utils import timezone

class ConsultModelSerializer(serializers.Serializer):
    """Serializer which voter with be assigned to a poll"""
    
    expiration = serializers.DateTimeField()

    def validate_expiration(self, data):
        """Expiration datetime must be in future, and during the poll period"""
        now = timezone.now()
        poll = self.context["poll"]
        if now > data:
            raise serializers.ValidationError("Expiration datetime must not happened")
        if data < poll.start_datetime:
            raise serializers.ValidationError("Expiration datetime must be after the start")
        if data > poll.end_datetime:
            raise serializers.ValidationError("Expiration datetime must be before the end")
        return data

    def create(self,data):
        """Voter has assigned a poll and generated a token"""
        poll = self.context["poll"]
        voter = self.context["voter"]
        consult = ConsultModel.objects.create(poll = poll, voter = voter, expiration = data['expiration'])
        return consult.token, consult.expiration


class ConsultTokenSerializer(serializers.Serializer):
    """Chief login serializer. """

    token = serializers.CharField(max_length=15)
