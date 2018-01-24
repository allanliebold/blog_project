"""blog view definitions."""

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """Definition of hello view."""
    return render(request, 'home.html')
