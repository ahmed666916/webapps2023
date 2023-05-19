from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transactions, name='transactions'),
    path('payment-requests/', views.payment_requests, name='payment_requests'),
    path('make-payment/', views.make_payment, name='make_payment'),
    path('request-payment/', views.request_payment, name='request_payment'),
    path('transaction-report/', views.transaction_report, name='transaction_report'),
    
]
