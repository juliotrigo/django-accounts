# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.shortcuts import render
from django.views.i18n import set_language

DJANGO_LANGUAGE = 'django_language'
LANGUAGE_FIELD = 'language'

@login_required
def profile(request):
    """Custom profile view."""
    return render(request, 'accounts/profile.html')

def custom_login(request, *args, **kwargs):
    """Custom login function which wraps Django's login view."""
    response = login(request, *args, **kwargs)
    
    # Set django_langauge in session: use user's language
    custom_user = request.user
    if custom_user.is_authenticated():
        if custom_user.language:
            request.session[DJANGO_LANGUAGE] = custom_user.language
    
    return response

def custom_logout(request, *args, **kwargs):
    """Custom login function which wraps Django's logout view."""
    # Get current language
    session_lan = ''
    if DJANGO_LANGUAGE in request.session:
        if request.session[DJANGO_LANGUAGE]:
            session_lan = request.session[DJANGO_LANGUAGE]
    
    response = logout(request, *args, **kwargs)
    
    # Restore the language
    if session_lan:
        request.session[DJANGO_LANGUAGE] = session_lan
    
    return response

def custom_i18n(request, *args, **kwargs):
    """Custom i18n view which wraps Django's set_language view."""
    response = set_language(request, *args, **kwargs)
    
    # Save user's language
    custom_user = request.user
    session_lan = request.session[DJANGO_LANGUAGE]
    if custom_user.is_authenticated():
        if session_lan:
            if custom_user.language != session_lan:
                custom_user.language = session_lan 
                custom_user.save(update_fields=[LANGUAGE_FIELD])
    
    return response