from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets

from .models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username: ")
    email = forms.EmailField(label="Email: ")
    password1 = forms.CharField(label="Password: ",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password:",widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError("Password do not match.")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and underscore')
        try:
            User.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError("Username is already taken")

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
                    'name',
                    'email',
                    'message'
                ]
    
    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)