# -*- coding: utf-8 -*-

"""accounts user forms."""

from django import forms
from django.contrib import auth

from accounts.models import CustomUser

class CustomUserCreationForm(auth.forms.UserCreationForm):
    """A form to create users."""
    
    #https://groups.google.com/forum/?fromgroups=#!topic/django-users/kOVEy9zYn5c
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    
    class Meta(auth.forms.UserCreationForm.Meta):
        model = CustomUser

class CustomUserChangeForm(auth.forms.UserChangeForm):
    """A form to update users."""
    
    class Meta(auth.forms.UserChangeForm.Meta):
        model = CustomUser