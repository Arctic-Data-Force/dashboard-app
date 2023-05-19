from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('', index, name='index'),
    path('championships/create/', create_championship, name='create_championship'),
]