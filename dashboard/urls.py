from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('', index, name='index'),
    path('championships/<int:championship_id>', show_championship, name='show_championship'),
    path('championships/create/', create_championship, name='create_championship'),
]