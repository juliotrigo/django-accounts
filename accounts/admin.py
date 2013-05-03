# -*- coding: utf-8 -*-

"""accounts admin."""

from django.contrib import admin
from django.contrib import auth

from accounts.models import ExtendedUser
from accounts.forms import ExtendedUserCreationForm, ExtendedUserChangeForm

class ExtendedUserAdmin(auth.admin.UserAdmin):
    """ExtendedUser Admin."""
    
    form = ExtendedUserChangeForm
    add_form = ExtendedUserCreationForm

admin.site.register(ExtendedUser, ExtendedUserAdmin)