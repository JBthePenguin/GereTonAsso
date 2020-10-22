from memberapp.models import Member, Association
from memberapp.filters import MemberFilter, AssosFilter
from django_filters.views import FilterView
from django.conf import settings


class MemberListView(FilterView):
    """Subclass of django_filters.views.FilterView to list members."""
    model = Member
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
        context['nav_members'] = 'active'
        context.update(settings.DEFAULT_CONTEXT)
        return context


class AssoListView(FilterView):
    """Subclass of django_filters.views.FilterView to list associations."""
    model = Association
    template_name = "visitapp/asso_list.html"
    filterset_class = AssosFilter
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
                context['object_list'] = Association.objects.all()
        context['page_title'] = 'Assos amies'
        context['nav_asso'] = 'active'
        context.update(settings.DEFAULT_CONTEXT)
        return context
