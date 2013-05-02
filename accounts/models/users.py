# -*- coding: utf-8 -*-

"""accounts user models."""

from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    """
    Extended user model with some extra fields.
    """
    
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta(AbstractUser.Meta):
        app_label = 'accounts'
