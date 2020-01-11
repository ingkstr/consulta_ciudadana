from django.db import models

from administration.models import Voter,Poll
from access.managers import ConsultManager

class ConsultModel(models.Model):
    """Asociation of voter with a poll"""
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    expiration = models.DateTimeField()
    token = models.CharField(max_length=15, unique=True)
    answered = models.BooleanField(default = False)

    objects = ConsultManager()

    class Meta:
        unique_together = (("voter", "poll"),)
