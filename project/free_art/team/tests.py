from django.test import TestCase
from team.models import Developer, Tester

# Create your tests here.
class TestDeveloper(TestCase):

    def setUp(self):
        dev = Developer.objects.create(name='Vasia',role='Guru')
        dev_re = Developer.objects.create(name='Va')

    def test_str(self):
        dev = Developer.objects.get(name='Vasia')
        dev_re = Developer.objects.get(name='Va')
        self.assertEqual(str(dev),'Vasia - Guru')
        self.assertEqual(str(dev_re),'Va')

class TestTester(TestCase):

    def setUp(self):
        tester = Tester.objects.create(name='Test')

    def test_str(self):
        tester = Tester.objects.get(name='Test')
        self.assertEqual(str(tester),'Test')