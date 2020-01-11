from rest_framework import serializers

# Models
from administration.models import Poll


class PollBriefModelSerializer(serializers.ModelSerializer):
    """Chief model serializer."""
    class Meta:
        """Meta class."""
        model = Poll
        fields = (
            'name',
            'slug',
            'start_datetime',
            'end_datetime',
        )
