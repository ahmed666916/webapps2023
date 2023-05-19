from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transactions, name='transactions'),
    path('payment-requests/', views.payment_requests, name='payment_requests'),
]
