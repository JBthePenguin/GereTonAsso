from django.shortcuts import render
from memberapp.models import Member
from visitapp.filters import MemberFilter
from django_filters.views import FilterView


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


class MemberListView(FilterView):

    model = Member
    paginate_by = 100
    template_name = "visitapp/member_list.html"
    filterset_class = MemberFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Membres'
        context.update(DEFAULT_CONTEXT)
        return context
