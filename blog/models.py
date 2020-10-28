from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models 
from django.template.defaultfilters import slugify



class Author(models.Model):
    """ Data table to store acs bloggers details"""
    posted_by = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,) 
    full_name = models.CharField(primary_key=True, max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Orders data table by publication dates 
        ordering = ['full_name']

    def __str__(self):
        # Outputs string of model object.
        return self.full_name
        
    def get_absolute_url(self):
        #Identifies url of individual posts by its template
        #specify where to send the user after successfully submitting the form
        return reverse('author_detail', args=[str(self.id)])  

class Post(models.Model):
    """ Data attributes needed for the creation
        of a new blog entry on the acs site. """
    # A single blog post can have many authors
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    additional_authors = models.CharField(blank=True, max_length=50,
                                          help_text='This field is optional')
    published_date = models.DateField()
    modified_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255, help_text='Enter the blog post headline')
    tagline = models.CharField(max_length=80)
    blog_content = models.TextField()
    photo = models.ImageField(upload_to='uploads/', blank=True)
    blog_content_file = models.FileField(upload_to='uploads/', blank=True)
    
  
    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return f'{self.author}, {self.published_date}, {self.tagline}, {self.blog_content}'                          
   
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

