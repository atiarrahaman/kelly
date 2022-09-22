from django import forms
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets


class  Register(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model= User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
        labels={
            'email':'Email'
        }

class ChangepassForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields='__all__'



class Userchage(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=[
            'username','email','first_name','last_name',
        ]

class UseradminchageForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'