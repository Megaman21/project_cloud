from django import forms
from django.contrib.auth.forms import UserCreationForm
from megamaninn.models import Customer


class SignUpForm(UserCreationForm):


    class Meta:
        model = Customer
        fields = ('name','email','password',)