from django.contrib import admin
from treasuryapp.models import Transaction, MoneyDeposit, MoneyWithdrawal


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'wording', 'date', 'bank_entry', 'bank_exit',
        'fund_entry', 'fund_exit']


@admin.register(MoneyDeposit)
class MoneyDepositAdmin(admin.ModelAdmin):
    list_display = ['amount', 'depositor', 'date']


@admin.register(MoneyWithdrawal)
class MoneyWithdrawalAdmin(admin.ModelAdmin):
    list_display = ['amount', 'withdrawer', 'date']
