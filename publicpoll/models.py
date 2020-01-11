from django.db import models

from administration.models import Poll
from access.managers import ConsultManager

class Statistics(models.Model):
    """Statistics counting total answers"""
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.IntegerField()
    true_counter = models.IntegerField(default=0)
    false_counter = models.IntegerField(default=0)

    class Meta:
        unique_together = (("poll","question"),)
