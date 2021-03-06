from django.contrib import admin
from loanapp.models import LoanMadeToMemberMaterial


@admin.register(LoanMadeToMemberMaterial)
class LoanMadeToMemberMaterialAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in LoanMadeToMemberMaterial._meta.get_fields()]

    def get_form(self, request, obj=None, **kwargs):
        """
        Not allow to add, delete, change material
        """
        form = super(LoanMadeToMemberMaterialAdmin, self).get_form(
            request, obj, **kwargs)
        for field_name in ["lender", "borrower", "material"]:
            form.base_fields['material'].widget.can_add_related = False
            form.base_fields['material'].widget.can_delete_related = False
            form.base_fields['material'].widget.can_change_related = False
        return form
