from memberapp.models import Member, Association
from memberapp.filters import MemberFilter
from django_filters.views import FilterView
from django.views.generic.list import ListView
from django.conf import settings


class MemberListView(FilterView):
    """Subclass of django_filters.views.FilterView to list members."""
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
        context.update(settings.DEFAULT_CONTEXT)
        return context


class AssoListView(ListView):
    """Subclass of django_filters.views.FilterView to list associations."""
    model = Association
    paginate_by = 100
    template_name = "visitapp/asso_list.html"
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        """Override original one to update the context."""
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Assos amies'
        context.update(settings.DEFAULT_CONTEXT)
        return context
