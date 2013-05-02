# -*- coding: utf-8 -*-

"""accounts admin."""

from django import forms
from django.contrib import admin
from django.contrib import auth

from accounts.models import ExtendedUser

class ExtendedUserCreationForm(auth.forms.UserCreationForm):
    """A form for creating users."""
    
    #https://groups.google.com/forum/?fromgroups=#!topic/django-users/kOVEy9zYn5c
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            ExtendedUser._default_manager.get(username=username)
        except ExtendedUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    
    class Meta(auth.forms.UserCreationForm.Meta):
        model = ExtendedUser

class ExtendedUserChangeForm(auth.forms.UserChangeForm):
    """A form for updating users."""
    
    class Meta(auth.forms.UserChangeForm.Meta):
        model = ExtendedUser

class ExtendedUserAdmin(auth.admin.UserAdmin):
    """ExtendedUser Admin."""
    
    form = ExtendedUserChangeForm
    add_form = ExtendedUserCreationForm

admin.site.register(ExtendedUser, ExtendedUserAdmin)