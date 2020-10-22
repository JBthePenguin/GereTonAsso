from django import forms
import django_filters
from treasuryapp.models import Transaction, MoneyDeposit, MoneyWithdrawal
from memberapp.models import Member


class TransactionFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    wording = django_filters.CharFilter(
        lookup_expr='icontains', label='Libellé contenant')
    date_before = django_filters.DateFilter(
        method='filter_date_lte', label='Opérations avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_after = django_filters.DateFilter(
        method='filter_date_gte', label='Opérations après',
        widget=forms.DateInput(attrs={'type': 'date'}))

    def filter_date_lte(self, queryset, name, value):
        return queryset.filter(date__lte=value).order_by('date')

    def filter_date_gte(self, queryset, name, value):
        return queryset.filter(date__gte=value).order_by('date')

    class Meta:
        model = Transaction
        fields = [
            'wording']


class DepositFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    depositor = django_filters.ModelChoiceFilter(
        queryset=Member.objects.all())
    date_before = django_filters.DateFilter(
        method='filter_date_lte', label='Dépôts avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_after = django_filters.DateFilter(
        method='filter_date_gte', label='Dépôts après',
        widget=forms.DateInput(attrs={'type': 'date'}))

    def filter_date_lte(self, queryset, name, value):
        return queryset.filter(date__lte=value).order_by('date')

    def filter_date_gte(self, queryset, name, value):
        return queryset.filter(date__gte=value).order_by('date')

    class Meta:
        model = MoneyDeposit
        fields = ['depositor']


class WithdrawalFilter(django_filters.FilterSet):
    """Subclass of django_filters.FilterSet """
    withdrawer = django_filters.ModelChoiceFilter(
        queryset=Member.objects.all())
    date_before = django_filters.DateFilter(
        method='filter_date_lte', label='Dépôts avant',
        widget=forms.DateInput(attrs={'type': 'date'}))
    date_after = django_filters.DateFilter(
        method='filter_date_gte', label='Dépôts après',
        widget=forms.DateInput(attrs={'type': 'date'}))

    def filter_date_lte(self, queryset, name, value):
        return queryset.filter(date__lte=value).order_by('date')

    def filter_date_gte(self, queryset, name, value):
        return queryset.filter(date__gte=value).order_by('date')

    class Meta:
        model = MoneyWithdrawal
        fields = ['withdrawer']
