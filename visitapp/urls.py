from django.urls import path
from visitapp.views import home
from memberapp.views import MemberListView, AssoListView

urlpatterns = [
    path('', home, name='home'),
    path('membres/', MemberListView.as_view(), name='members'),
    path('assos-amies/', AssoListView.as_view(), name='associations'), ]
