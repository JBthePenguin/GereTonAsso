from django.shortcuts import render
from django.conf import settings


def home(request):
    """Return the home page."""
    context = {
        'page_title': 'Accueil',
        'nav_home': 'active'
    }
    context.update(settings.DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', context)
