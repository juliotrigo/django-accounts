from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def profile(request):
    context = {'user': request.user}
    return render_to_response('accounts/profile.xhtml', context)