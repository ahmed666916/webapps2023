from django.shortcuts import render
from .models import Transaction, PaymentRequest

def transactions(request):
    transactions = Transaction.objects.filter(sender=request.user) | Transaction.objects.filter(recipient=request.user)
    return render(request, 'transactions.html', {'transactions': transactions})

def payment_requests(request):
    requests = PaymentRequest.objects.filter(recipient=request.user)
    return render(request, 'payment_requests.html', {'requests': requests})
