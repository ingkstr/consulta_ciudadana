
from rest_framework import serializers

# Models
from administration.models import Voter

from access.serializers.poll import PollBriefModelSerializer


class VoterModelSerializer(serializers.ModelSerializer):
    """Chief model serializer."""
    class Meta:
        """Meta class."""
        model = Voter
        fields = (
            'cid',
            'name',
            'address',
            'born_date',
        )
