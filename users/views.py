from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

"""using Django’s generic CreateView here and telling it to use our CustomUserCreationForm,
to redirect to login once a user signs up successfully, and that our template is named
signup.html """

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'