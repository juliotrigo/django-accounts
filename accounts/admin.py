# -*- coding: utf-8 -*-

"""accounts admin."""

from django.contrib import admin
from django.contrib import auth

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(auth.admin.UserAdmin):
    """CustomUser Admin."""
    
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)