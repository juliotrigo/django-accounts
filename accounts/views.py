from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def profile(request):
    return render_to_response('accounts/profile.xhtml', 
                              context_instance=RequestContext(request))