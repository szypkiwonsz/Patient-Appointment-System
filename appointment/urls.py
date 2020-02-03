from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='appointment-index'),
    path('uslugi/', views.uslugi, name='appointment-uslugi'),
    path('cennik/', views.uslugi, name='appointment-cennik'),
    path('o_mnie/', views.uslugi, name='appointment-o_mnie'),
]