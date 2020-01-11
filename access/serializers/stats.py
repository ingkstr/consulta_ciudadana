from rest_framework import serializers

from publicpoll.models import Statistics

class StatsModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    class Meta:
        """Meta class."""
        model = Statistics
        fields = (
            'question',
            'true_counter',
            'false_counter',
        )
