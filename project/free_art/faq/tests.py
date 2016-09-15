from django.test import TestCase
from faq.models import Faq

# Create your tests here.
class TestFaq(TestCase):

    def setUp(self):
        faq = Faq.objects.create(question='What', answer='Ups')

    def test_str(self):
        faq = Faq.objects.get(question='What')
        self.assertEqual(str(faq),'What')