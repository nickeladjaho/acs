from django.test import TestCase
from django.urls import reverse
from .models import Promotion


class PromotionModelTest(TestCase):

    def setUp(self):   
        Promotion.objects.create(
        title='let this be a title',
        event_description = 'this is my sample event'
        )
    
    def test_text_content(self):
        single_event = Promotion.objects.get(id=1)
        expected_object_name = f'{single_event.title}'
        self.assertEqual(expected_object_name, 'let this be a title')


"""
add text string repr and other tests, like views 200

    def test_string_representation(self):
        blogger = Post(tagline='teaser tag')
        self.assertEqual(str(blogger), blogger.tagline)

"""