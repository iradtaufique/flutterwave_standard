from django.shortcuts import redirect, render

from payment.forms import CustomPaymentForm
from payment.pay import process_payment

# Create your views here.

def custom_payment(request):
    form = CustomPaymentForm()
    if request.method=='POST':
        form =CustomPaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return redirect(process_payment(amount, name, email))

    context = {'form': form}
    return render(request, 'payment.html', context)