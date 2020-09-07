from django.shortcuts import render

DEFAULT_CONTEXT = {
    'title_site': 'Gère Ton Asso',
    'nav_brand': 'Mon asso',
}


def home(request):
    # return the home page
    context = {
        'page_title': 'Home',
        'home_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', context)
