from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """"Create forum to edit users info in admin
        and list of user musts to sing up as a user"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'username', 'email', 'degree', 'uni_year', 'is_staff', ]
    



admin.site.register(CustomUser, CustomUserAdmin) 