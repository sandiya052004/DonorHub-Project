

from django import forms
from .models import DonationRequest

class DonationRequestForm(forms.ModelForm):
    class Meta:
        model = DonationRequest
        fields = ['organization', 'donation_type_requested', 'additional_details']
class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
