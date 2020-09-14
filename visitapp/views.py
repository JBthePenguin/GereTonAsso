from django.shortcuts import render
from memberapp.models import Member
from visitapp.filters import MemberFilter
from django_filters.views import FilterView


DEFAULT_CONTEXT = {
    'title_site': 'Gère Ton Asso',
    'nav_brand': 'Mon asso',
}


def home(request):
    """Return the home page."""
    context = {
        'page_title': 'Home',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', context)


class MemberListView(FilterView):
    """Subclass of django_filters.views.FilterView"""
    model = Member
    paginate_by = 100
    template_name = "visitapp/member_list.html"
    filterset_class = MemberFilter
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        """Override original one to update the context."""
        context = super().get_context_data(**kwargs)
        context['display_form'] = 'none'
        if self.request.GET:
            # filter form submitted
            context['display_form'] = 'block'
            if self.request.GET.get('reset'):
                # filter form reseted
                context['display_form'] = 'none'
                context['filter'] = self.filterset_class()
                context['object_list'] = Member.objects.all()
        context['page_title'] = 'Membres'
        context.update(DEFAULT_CONTEXT)
        return context
