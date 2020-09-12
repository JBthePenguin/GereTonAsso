from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from memberapp.models import Member

DEFAULT_CONTEXT = {
    'title_site': 'Gère Ton Asso',
    'nav_brand': 'Mon asso',
}


def home(request):
    # return the home page
    context = {
        'page_title': 'Home',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', context)


class MemberListView(ListView):

    model = Member
    paginate_by = 100
    template_name = "visitapp/member_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['page_title'] = 'Membres'
        context.update(DEFAULT_CONTEXT)
        return context
