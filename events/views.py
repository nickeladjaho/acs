from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Promotion



class PromotionListView(ListView):
    model = Promotion
    template_name = 'events_main.html'
    context_object_name = 'all_events_list'

""" access to individual records in promotion mode

class PostDetailView(DetailView):
    # Allows a user to view the contents an individual blog entry
    model = Post
    template = 'post_detail.html'
"""

