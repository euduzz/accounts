from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm

#Create your forms here
class LoginForm(AuthenticationForm):
    username = forms.CharField(
    	widget = TextInput(
    		attrs={
    			'class':'form-control',
    			'placeholder': 'Username'
    		}
    	)
    )
    password = forms.CharField(
    	widget = PasswordInput(
    		attrs={
    			'class':'form-control',
    			'placeholder': '*******'
    		}
    	)
    )
