import email
from django import forms


class CustomPaymentForm(forms.Form):
    amount = forms.IntegerField()
    name = forms.CharField(max_length=50)
    email = forms.EmailField()