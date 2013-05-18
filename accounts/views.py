# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def profile(request):
    """Custom profile view."""
    return render_to_response('accounts/profile.xhtml', 
                              context_instance=RequestContext(request))

def custom_login(request, *args, **kwargs):
    """Custom login function which wraps Django's login view."""
    response = login(request, *args, **kwargs)
    #TODO
    return response

def custom_logout(request, *args, **kwargs):
    """Custom login function which wraps Django's logout view."""
    #TODO
    return logout(request, *args, **kwargs)
