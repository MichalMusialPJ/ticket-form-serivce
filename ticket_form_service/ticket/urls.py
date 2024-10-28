from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.ticket_form_view, name='ticket_form'),
]
