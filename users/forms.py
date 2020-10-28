from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """ Able to edit user field at a instantly"""
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name','last_name', 'username', 'email', 'uni_year', 'degree',)


class CustomUserChangeForm(UserChangeForm):
    """display the custom user sign in admin"""
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'uni_year', 'degree',)
        