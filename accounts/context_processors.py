# -*- coding: utf-8 -*-

"""accounts context processors.

A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from __future__ import unicode_literals

def url(request):
    """
    Adds url-related context variables to the context.
    """
    return {'get_full_path': request.get_full_path()}