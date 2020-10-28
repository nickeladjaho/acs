from django.shortcuts import render
from django.views.generic import TemplateView

# Hardcoded pages in template engine

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'   


class ContactPageView(TemplateView):
    template_name = 'contact.html'

