from django.conf import settings
from django_filters.views import FilterView
from inventoryapp.models import Material, Recovery
from inventoryapp.filters import MaterialFilter


class MaterialListView(FilterView):
    """Subclass of django_filters.views.FilterView to list members."""
    model = Material
    paginate_by = 100
    template_name = "visitapp/material_list.html"
    filterset_class = MaterialFilter
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
                context['object_list'] = Material.objects.all()
        context['page_title'] = 'Matériels'
        context['nav_materials'] = 'active'
        # recoveries receipts links
        recoveries_links = {}
        recoveries = Recovery.objects.all()
        for recovery in recoveries:
            recoveries_links[recovery.material] = recovery.receipt.url
        context['recoveries'] = recoveries_links
        context.update(settings.DEFAULT_CONTEXT)
        return context
