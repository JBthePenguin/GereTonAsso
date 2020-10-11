from django import forms
from django.utils.translation import gettext as _
from inventoryapp.models import Material
import django_filters


# class MyBooleanWidget(forms.Select):
#     """Convert true/false values into the internal Python True/False.
#     This can be used for AJAX queries that pass true/false from JavaScript's
#     internal types through.
#     """
#
#     def __init__(self, attrs=None):
#         choices = (
#             ('', _('-------')), ('true', _('Yes')), ('false', _('No')))
#         super().__init__(attrs, choices)
#
#     def render(self, name, value, attrs=None, renderer=None):
#         try:
#             value = {
#                 True: 'true',
#                 False: 'false',
#                 '1': 'true',
#                 '0': 'false'
#             }[value]
#         except KeyError:
#             value = ''
#         return super().render(name, value, attrs, renderer=renderer)
#
#     def value_from_datadict(self, data, files, name):
#         value = data.get(name, None)
#         if isinstance(value, str):
#             value = value.lower()
#
#         return {
#             '1': True,
#             '0': False,
#             'true': True,
#             'false': False,
#             True: True,
#             False: False,
#         }.get(value, None)


class MaterialFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    reference = django_filters.CharFilter(
        lookup_expr='icontains', label='Référence contenant')
    value_less_than = django_filters.NumberFilter(
        method='filter_value_lte', label='Valeur inférieure à',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 0.01}))
    value_more_than = django_filters.NumberFilter(
        method='filter_value_gte', label='Valeur supérieure à',
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'step': 0.01}))
    CATEGORY_CHOICES = [
        ("A", "Association"),
        ("N", "Numérique"),
        ("M", "Musique"),
        ("E", "Énergie"),
        ("C", "Consommation")
    ]
    category = django_filters.ChoiceFilter(
        choices=CATEGORY_CHOICES, label='Catégorie')
    ACQUISITION_CHOICES = [
        ("R", "Récupération"),
        ("P", "Prêt"),
        ("A", "Achat"),
        ("D", "Don")
    ]
    acquisition = django_filters.ChoiceFilter(
        choices=ACQUISITION_CHOICES, label='Acquisition')
    STATUT_CHOICES = [
        ("A", "Dispo"),
        ("P", "Prêté"),
        ("R", "Rendu"),
        ("D", "Donné"),
        ("V", "Vendu")
    ]
    statut = django_filters.ChoiceFilter(choices=STATUT_CHOICES, label='État')

    def filter_value_lte(self, queryset, name, value):
        return queryset.filter(value__lte=value).order_by(
            'value')

    def filter_value_gte(self, queryset, name, value):
        return queryset.filter(value__gte=value).order_by(
            'value')

    class Meta:
        model = Material
        fields = [
            'reference', 'value_less_than', 'value_more_than',
            'category', 'acquisition', 'statut']
