from django.forms import ModelForm
from inventoryapp.models import Material


class MaterialAdminForm(ModelForm):

    class Meta:
        model = Material
        exclude = ('acquisition', 'statut')
