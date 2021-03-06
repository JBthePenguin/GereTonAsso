from django import forms
from inventoryapp.models import Material, Recovery
from memberapp.models import Member
import django_filters


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
        ("V", "Vendu"),
        ("H", "HS"),
        ("J", "Jeté")
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


class RecoveryFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    material__reference = django_filters.CharFilter(
        lookup_expr='icontains', label='Référence matériel contenant')
    recuperator = django_filters.ModelChoiceFilter(
        queryset=Member.objects.all())
    date_before = django_filters.DateFilter(
        method='filter_date_lte', label='Récupéré avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_after = django_filters.DateFilter(
        method='filter_date_gte', label='Récupéré après',
        widget=forms.DateInput(attrs={'type': 'date'}))

    def filter_date_lte(self, queryset, name, value):
        return queryset.filter(date__lte=value).order_by('date')

    def filter_date_gte(self, queryset, name, value):
        return queryset.filter(date__gte=value).order_by('date')

    class Meta:
        model = Recovery
        fields = [
            'material__reference', 'recuperator']
