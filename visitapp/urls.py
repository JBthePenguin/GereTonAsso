from django.urls import path
from visitapp.views import home

urlpatterns = [
    path('', home, name='home'), ]
