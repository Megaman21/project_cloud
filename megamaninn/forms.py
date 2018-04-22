from django import forms
from django.contrib.auth.forms import UserCreationForm
from megamaninn.models import Customer


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, help_text='Optional.')
    password = forms.CharField(max_length=50, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Customer
        fields = ('name','email','password',)