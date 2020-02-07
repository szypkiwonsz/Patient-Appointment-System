from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='appointment-index'),
    path('uslugi/', views.uslugi, name='appointment-uslugi'),
    path('cennik/', views.cennik, name='appointment-cennik'),
    path('o_mnie/', views.o_mnie, name='appointment-o_mnie')
]