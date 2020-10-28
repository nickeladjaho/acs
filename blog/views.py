from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Post


class PostListView(ListView):
    # Displays most recent blog entries on page
    model = Post
    template_name = 'blog/post_list.html'
    #context_object_name = 'all_posts_list'   # explicitly name the context object in our view 
    """
    def get_queryset(self):
        # override the get_queryset() method to change the list of records returned
        return Post.objects.filter()[:]
    """
    """ def get_context_data(self, **kwargs):
        
        #we override get_context_data() in order to pass additional context variables to the template
        #The view passes the context (list of posts) by default as object_list and post_list aliases

        # Call the base implementation first to get the context
        context = super(PostListView, self).get_context_data(**kwargs)          # First get the existing context from our superclass
        # Create any data and add it to the context (can be used as template variable)
        context['some_data'] = 'This is just some data'                         # Then we add your new context information
        return context                                                          # Then return the new (updated) context """

class PostDetailView(DetailView):
    # Allows a user to view the contents an individual blog entry
    model = Post
    template_name = 'blog/post_detail.html'
    """
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['txts'] = Post.objects.get(title='Example 1')
        return context
    """
    

