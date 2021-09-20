from django.shortcuts import render
from .models import Payment

# Create your views here.
def Payments(request):
    context = {
        'payment':Payment.objects.all()
    }
    return render(request, 'payments/payment.html', context)