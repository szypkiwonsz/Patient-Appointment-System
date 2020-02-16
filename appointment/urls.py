from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_appointment, name='appointment-make_appointment'),
    path('cancel_appointment/', views.cancel_appointment, name='appointment-cancel_appointment'),
    path('confirm_cancel_appointment/', views.confirm_cancel_appointment, name='appointment-confirm_cancel_appointment')
]