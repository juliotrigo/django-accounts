# -*- coding: utf-8 -*-

"""accounts user models."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class CustomUser(AbstractUser):
    """
    Custom user model.
    
    The custom user model contains some extra fields.
    """
    
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True,
                                     help_text=_("User's date of birth."))
    language = models.CharField(_("language"), max_length=5, blank=True, choices=settings.LANGUAGES,
                                help_text=_("User's selected language."))
    
    class Meta(AbstractUser.Meta):
        app_label = 'accounts'