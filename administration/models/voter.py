from django.db import models

from administration.models import Poll

class Voter(models.Model):
    """Voter model class"""
    cid = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    born_date = models.DateField()
    alive = models.BooleanField()
    registered_date = models.DateField(auto_now_add=True)
