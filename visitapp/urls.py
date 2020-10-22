from django.urls import path
from visitapp.views import home
from memberapp.views import MemberListView, AssoListView
from inventoryapp.views import MaterialListView, RecoveryListView
from treasuryapp.views import (
    TransactionListView, DepositListView, WithdrawalListView)

urlpatterns = [
    path('', home, name='home'),
    path('membres/', MemberListView.as_view(), name='members'),
    path('assos-amies/', AssoListView.as_view(), name='associations'),
    path('inventaire/', MaterialListView.as_view(), name='materials'),
    path(
        'inventaire/recuperations/', RecoveryListView.as_view(),
        name='recoveries'),
    path('tresorerie/', TransactionListView.as_view(), name='transactions'),
    path('tresorerie/depots/', DepositListView.as_view(), name='deposits'),
    path(
        'tresorerie/retraits/', WithdrawalListView.as_view(),
        name='withdrawals')
]
