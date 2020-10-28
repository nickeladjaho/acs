from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Author, Post


class BlogTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='exampleuser',
            password='mypassowrd',
        )

        self.author = Author.objects.create(
            posted_by = self.user,
            full_name='jon doe', 
        )

        self.post = Post.objects.create(
            author = self.author.posted_by,
            published_date = '2019-09-28',
            title = 'Some title',
            tagline = 'teaser tag',
            blog_content = 'this is all i will be writing today',
        )



    def test_string_representation(self):
        blogger = Post(tagline='teaser tag')
        self.assertEqual(str(blogger), blogger.tagline)


#test author model new class to test it?
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
#https://docs.djangoproject.com/en/2.2/topics/testing/overview/
#http://www.learningaboutelectronics.com/Articles/How-to-access-and-use-the-Python-shell-with-Django.php

