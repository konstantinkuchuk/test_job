from django.urls import path
from .views import *


urlpatterns = [
    path('menu/', menu, name='menu'),
    path('test_tree/', test_tree, name='test_tree'),
    path('open/', open, name='open'),
]


