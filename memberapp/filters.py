from django import forms
from django.utils.translation import gettext as _
from memberapp.models import Member, Association
import django_filters


class MyBooleanWidget(forms.Select):
    """Convert true/false values into the internal Python True/False.
    This can be used for AJAX queries that pass true/false from JavaScript's
    internal types through.
    """

    def __init__(self, attrs=None):
        choices = (
            ('', _('-------')), ('true', _('Yes')), ('false', _('No')))
        super().__init__(attrs, choices)

    def render(self, name, value, attrs=None, renderer=None):
        try:
            value = {
                True: 'true',
                False: 'false',
                '1': 'true',
                '0': 'false'
            }[value]
        except KeyError:
            value = ''
        return super().render(name, value, attrs, renderer=renderer)

    def value_from_datadict(self, data, files, name):
        value = data.get(name, None)
        if isinstance(value, str):
            value = value.lower()

        return {
            '1': True,
            '0': False,
            'true': True,
            'false': False,
            True: True,
            False: False,
        }.get(value, None)


class MemberFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    last_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Nom contenant')
    first_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Prénom contenant')
    email = django_filters.CharFilter(
        lookup_expr='icontains', label='Email contenant')
    phone = django_filters.CharFilter(
        label='Téléphone contenant', method='filter_phone')
    date_of_birth_after = django_filters.DateFilter(
        method='filter_birth_gte', label='Né(e) après',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_of_birth_before = django_filters.DateFilter(
        method='filter_birth_lte', label='Né(e) avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_joined_after = django_filters.DateTimeFilter(
        method='filter_joined_gte', label='Inscrit(e) après',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_joined_before = django_filters.DateTimeFilter(
        method='filter_joined_lte', label='Inscrit(e) avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    active = django_filters.BooleanFilter(widget=MyBooleanWidget())
    GRADE_CHOICES = [
        ("A", "Adhérent"),
        ("H", "Honneur"),
        ("C", "Collège")
    ]
    grade = django_filters.ChoiceFilter(choices=GRADE_CHOICES, label='Statut')

    def filter_phone(self, queryset, name, value):
        s = []  # disregarding spaces
        for i in range(0, len(value)):
            s.append(value[i:i+1])
        return queryset.filter(phone__iregex='\\s*'.join(s))

    def filter_birth_gte(self, queryset, name, value):
        return queryset.filter(date_of_birth__gte=value).order_by(
            'date_of_birth')

    def filter_birth_lte(self, queryset, name, value):
        return queryset.filter(date_of_birth__lte=value).order_by(
            'date_of_birth')

    def filter_joined_gte(self, queryset, name, value):
        return queryset.filter(date_joined__date__gte=value).order_by(
            'date_joined')

    def filter_joined_lte(self, queryset, name, value):
        return queryset.filter(date_joined__date__lte=value).order_by(
            'date_joined')

    class Meta:
        model = Member
        fields = [
             'active', 'last_name', 'first_name', 'email', 'phone', 'grade']


class AssosFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    name = django_filters.CharFilter(
        lookup_expr='icontains', label='Nom contenant')
    email = django_filters.CharFilter(
        lookup_expr='icontains', label='Email contenant')
    phone = django_filters.CharFilter(
        label='Téléphone contenant', method='filter_phone')
    number_rna = django_filters.CharFilter(
        lookup_expr='icontains', label='Numéro RNA contenant')
    number_siren = django_filters.CharFilter(
        lookup_expr='icontains', label='Numéro SIREN contenant')

    def filter_phone(self, queryset, name, value):
        s = []  # disregarding spaces
        for i in range(0, len(value)):
            s.append(value[i:i+1])
        return queryset.filter(phone__iregex='\\s*'.join(s))

    class Meta:
        model = Association
        fields = [
             'name', 'email', 'phone', 'number_rna', 'number_siren']
