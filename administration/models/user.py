from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User extended from abstract. It will check if he is
    admin or voting chief."""

    is_staff = models.BooleanField(
        'He is staff',
        default=False,
        help_text='Set to true if he is staff'
    )

    is_voting_chief = models.BooleanField(
        'He is voting chief',
        default=True,
        help_text='Set to true when the user is voting chief'
    )

    is_voting_node = models.BooleanField(
        'User is used as voting node',
        default=True,
        help_text='Set to true when the user is used in a voting node'
    )

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'is_voting_chief', 'is_voting_node']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
