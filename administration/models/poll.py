from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import RegexValidator

class Poll(models.Model):
    """Model of poll with 10 questions"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=50,unique=True,validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9]+$',
                message='Slug must only have numbers, letters',
            ),])
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    question0 = models.TextField()
    question1 = models.TextField(blank=True,null=True)
    question2 = models.TextField(blank=True,null=True)
    question3 = models.TextField(blank=True,null=True)
    question4 = models.TextField(blank=True,null=True)
    question5 = models.TextField(blank=True,null=True)
    question6 = models.TextField(blank=True,null=True)
    question7 = models.TextField(blank=True,null=True)
    question8 = models.TextField(blank=True,null=True)
    question9 = models.TextField(blank=True,null=True)
    ready = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    modificated_date = models.DateField(auto_now_add=True)

    def clean(self):
        """Dates must be consistents and futures"""
        now = timezone.now()
        if self.start_datetime > self.end_datetime:
            raise ValidationError("Dates are incorrect")
        if now > self.start_datetime:
            raise ValidationError("Start datetime must not happened")
        if now > self.end_datetime:
            raise ValidationError("End datetime must not happened")

    def __str__(self):
        return self.name
