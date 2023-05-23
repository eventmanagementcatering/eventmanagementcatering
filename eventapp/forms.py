from django import forms
from eventapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact
class eventrequestform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=eventrequest 

class bookingform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=booking       

class signupform(UserCreationForm):
    class Meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=User
            