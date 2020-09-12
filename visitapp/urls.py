from django.urls import path
from visitapp.views import home, MemberListView

urlpatterns = [
    path('', home, name='home'),
    path('membres/', MemberListView.as_view(), name='members'), ]
