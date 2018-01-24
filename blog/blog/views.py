"""blog view definitions."""

from django.http import HttpResponse


def hello(request):
    """Definition of hello view."""
    return HttpResponse("Hello World")
