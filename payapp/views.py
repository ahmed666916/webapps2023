from django.shortcuts import render
from .models import Transaction, PaymentRequest

def make_payment(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        amount = request.POST.get('amount')
        recipient = User.objects.get(id=recipient_id)

        if recipient and recipient != request.user and request.user.balance >= amount:
            transaction = Transaction.objects.create(sender=request.user, recipient=recipient, amount=amount)
            request.user.balance -= amount
            recipient.balance += amount
            request.user.save()
            recipient.save()
            transaction.save()
            return redirect('payment_success')
    
    return render(request, 'make_payment.html', {'users': User.objects.exclude(id=request.user.id)})

def request_payment(request):
    if request.method == 'POST':
        requester_id = request.POST.get('requester')
        amount = request.POST.get('amount')
        requester = User.objects.get(id=requester_id)

        if requester and requester != request.user:
            payment_request = PaymentRequest.objects.create(requester=request.user, recipient=requester, amount=amount)
            payment_request.save()
            return redirect('payment_request_success')

    return render(request, 'request_payment.html', {'users': User.objects.exclude(id=request.user.id)})

def transactions(request):
    transactions = Transaction.objects.filter(sender=request.user) | Transaction.objects.filter(recipient=request.user)
    return render(request, 'transactions.html', {'transactions': transactions})

def payment_requests(request):
    requests = PaymentRequest.objects.filter(recipient=request.user)
    return render(request, 'payment_requests.html', {'requests': requests})

def transaction_report(request):
    transactions = Transaction.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
    return render(request, 'transaction_report.html', {'transactions': transactions})


