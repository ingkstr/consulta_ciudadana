"""Circle invitation managers."""

# Django
from django.db import models

# Utilities
import random
from string import ascii_uppercase, digits


class ConsultManager(models.Manager):
    """Consult manager. It creates token for voter consult"""

    CODE_LENGTH = 15

    def create(self, **kwargs):
        """Handle code creation."""
        pool = ascii_uppercase + digits
        token = kwargs.get('token', ''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(token=token).exists():
            token = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwargs['token'] = token
        return super(ConsultManager, self).create(**kwargs)
