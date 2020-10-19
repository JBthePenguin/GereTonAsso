from django.urls import path
from visitapp.views import home
from memberapp.views import MemberListView, AssoListView
from inventoryapp.views import MaterialListView, RecoveryListView

urlpatterns = [
    path('', home, name='home'),
    path('membres/', MemberListView.as_view(), name='members'),
    path('assos-amies/', AssoListView.as_view(), name='associations'),
    path('materiels/', MaterialListView.as_view(), name='materials'),
    path('recuperations/', RecoveryListView.as_view(), name='recoveries'), ]
