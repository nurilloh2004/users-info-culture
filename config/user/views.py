from django.shortcuts import render
from .models import Enterer


def home(request):
    """Function for home view."""
    return render(request, 'home.html')


def blog(request):
    """Blog for count users enterence."""
    return render(request, 'blog.html')
