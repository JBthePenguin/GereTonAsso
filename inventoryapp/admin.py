from django.contrib import admin
from inventoryapp.models import Material
from inventoryapp.forms import MaterialAdminForm


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = MaterialAdminForm
    list_display = ['reference', 'category', 'value', 'acquisition', 'statut']
