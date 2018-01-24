"""blog view definitions."""

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    """Definition of hello view."""
    return render(request, 'home.html')
