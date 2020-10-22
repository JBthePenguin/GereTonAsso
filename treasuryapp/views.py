from django.conf import settings
from django.db.models import Sum
from django_filters.views import FilterView
from decimal import Decimal
from treasuryapp.models import Transaction, MoneyDeposit, MoneyWithdrawal
from treasuryapp.filters import (
    TransactionFilter, DepositFilter, WithdrawalFilter)


class TransactionListView(FilterView):
    """Subclass of django_filters.views.FilterView to list recoveries."""
    model = Transaction
    template_name = "visitapp/transaction_list.html"
    filterset_class = TransactionFilter
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
                context['object_list'] = Transaction.objects.all()
        context['page_title'] = 'Trésorerie'
        context['nav_treasury'] = 'active'
        # total value
        if context['object_list']:
            TWOPLACES = Decimal(10) ** -2
            try:
                context['total_bank_entry'] = Decimal(
                    context['object_list'].aggregate(Sum('bank_entry')).get(
                        'bank_entry__sum')).quantize(TWOPLACES)
            except TypeError:
                context['total_bank_entry'] = Decimal('0').quantize(TWOPLACES)
            try:
                context['total_bank_exit'] = Decimal(
                    context['object_list'].aggregate(Sum('bank_exit')).get(
                        'bank_exit__sum')).quantize(TWOPLACES)
            except TypeError:
                context['total_bank_exit'] = Decimal('0').quantize(TWOPLACES)
            try:
                context['total_fund_entry'] = Decimal(
                    context['object_list'].aggregate(Sum('fund_entry')).get(
                        'fund_entry__sum')).quantize(TWOPLACES)
            except TypeError:
                context['total_fund_entry'] = Decimal('0').quantize(TWOPLACES)
            try:
                context['total_fund_exit'] = Decimal(
                    context['object_list'].aggregate(Sum('fund_exit')).get(
                        'fund_exit__sum')).quantize(TWOPLACES)
            except TypeError:
                context['total_fund_exit'] = Decimal('0').quantize(TWOPLACES)
            context['total_bank'] = context[
                'total_bank_entry'] - context['total_bank_exit']
            context['total_fund'] = context[
                'total_fund_entry'] - context['total_fund_exit']
            context['total'] = context[
                'total_bank'] + context['total_fund']
        context.update(settings.DEFAULT_CONTEXT)
        return context


class DepositListView(FilterView):
    """Subclass of django_filters.views.FilterView to list recoveries."""
    model = MoneyDeposit
    template_name = "visitapp/deposit_list.html"
    filterset_class = DepositFilter
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
                context['object_list'] = MoneyDeposit.objects.all()
        context['page_title'] = 'Dépôts à la banque'
        context['nav_treasury'] = 'active'
        # total value
        if context['object_list']:
            TWOPLACES = Decimal(10) ** -2
            context['total_amount'] = Decimal(context['object_list'].aggregate(
                Sum('amount')).get('amount__sum')).quantize(TWOPLACES)
        context.update(settings.DEFAULT_CONTEXT)
        return context


class WithdrawalListView(FilterView):
    """Subclass of django_filters.views.FilterView to list recoveries."""
    model = MoneyWithdrawal
    template_name = "visitapp/withdrawal_list.html"
    filterset_class = WithdrawalFilter
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
                context['object_list'] = MoneyWithdrawal.objects.all()
        context['page_title'] = 'Retraits à la banque'
        context['nav_treasury'] = 'active'
        # total value
        if context['object_list']:
            TWOPLACES = Decimal(10) ** -2
            context['total_amount'] = Decimal(context['object_list'].aggregate(
                Sum('amount')).get('amount__sum')).quantize(TWOPLACES)
        context.update(settings.DEFAULT_CONTEXT)
        return context
