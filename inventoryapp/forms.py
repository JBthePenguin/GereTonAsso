from django.forms import ModelForm
from inventoryapp.models import Material, Recovery


class MaterialAdminForm(ModelForm):

    class Meta:
        model = Material
        exclude = ('acquisition', 'statut')


class RecoveryAdminForm(ModelForm):

    class Meta:
        model = Recovery
        exclude = ('material', 'receipt')
