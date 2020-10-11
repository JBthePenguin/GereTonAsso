from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin
from django.db.models.deletion import ProtectedError
from django.utils.safestring import SafeString
from inventoryapp.models import Material, Recovery
from inventoryapp.forms import MaterialAdminForm


@admin.register(Recovery)
class RecoveryAdmin(ReverseModelAdmin):
    model = Recovery
    inline_type = 'tabular'
    inline_reverse = [
        ('material', {'fields': ['reference', 'value', 'category']})]
    save_as = True
    list_display = ['get_material', 'get_recuperator', 'date']
    list_display_links = None
    list_filter = ('date', )
    search_fields = (
        'material__reference', 'recuperator__last_name',
        'recuperator__first_name')

    def get_material(self, obj):
        return f"{obj.material.reference}"

    def get_recuperator(self, obj):
        return f"{obj.recuperator.last_name} {obj.recuperator.first_name}"

    def get_form(self, request, obj=None, **kwargs):
        """
        Not allow to add, delete, change recuperator.
        """
        form = super(RecoveryAdmin, self).get_form(
            request, obj, **kwargs)
        form.base_fields["recuperator"].widget.can_delete_related = False
        form.base_fields["recuperator"].widget.can_change_related = False
        form.base_fields["recuperator"].widget.can_add_related = False
        form.base_fields['recuperator'].label_from_instance = lambda obj: f"{obj.last_name} {obj.first_name}"
        return form

    def get_deleted_objects(self, objs, request):
        """Override to check if material is not Protected."""
        for obj in objs:
            try:
                obj.material.delete()
            except ProtectedError as e:
                material_protected_objects = list(e.protected_objects)
                if len(material_protected_objects) > 1:
                    material_protected_objects.remove(obj)
                    protected = []
                    for protected_obj in material_protected_objects:
                        obj_link = f'Le matériel {obj.material.reference} est lié à <a href="/admin/{protected_obj.__class__._meta.app_label}/{protected_obj.__class__.__name__.lower()}/{str(protected_obj.id)}/change/">{str(protected_obj)}</a>'
                        protected.append(SafeString(obj_link))
                    default_return = super(
                        RecoveryAdmin, self).get_deleted_objects(objs, request)
                    return (
                        default_return[0], default_return[1],
                        default_return[2], protected)
        return super(RecoveryAdmin, self).get_deleted_objects(objs, request)

    get_material.short_description = "Matériel"
    get_recuperator.short_description = "Récupérateur"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = MaterialAdminForm
    list_display = ['reference', 'category', 'value', 'acquisition', 'statut']
    list_filter = ('category', 'acquisition', 'statut')
    search_fields = ('reference', )
    actions = None

    def render_change_form(
            self, request, context, add=False, change=False,
            form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False,
        })
        return super().render_change_form(
            request, context, add, change, form_url, obj)
