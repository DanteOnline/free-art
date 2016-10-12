from django.test import TestCase
from how_to_use.models import Subject, Step

# Create your tests here.
class TestSubject(TestCase):

    def setUp(self):
        subj = Subject.objects.create(name='Subj test')
        step2 = Step.objects.create(number=2, name='step_second', description='desc', subject=subj)
        step1 = Step.objects.create(number=1, name='step_first', subject=subj)

    def test_str(self):
        subj = Subject.objects.get(name='Subj test')
        self.assertEqual(str(subj),'Subj test')

    def test_get_steps(self):
        subj = Subject.objects.get(name='Subj test')
        step2 = Step.objects.get(number=2, name='step_second', description='desc')
        step1 = Step.objects.get(number=1, name='step_first')

        steps = subj.get_steps()
        self.assertEqual(steps[0],step1)
        self.assertEqual(steps[1],step2)

class TestStep(TestCase):

    def setUp(self):
        subj = Subject.objects.create(name='Subj test')
        step2 = Step.objects.create(number=2,name='step_second',description='desc', subject=subj)
        step1 = Step.objects.create(number=1, name='step_first', subject=subj)

    def test_str(self):
        step2 = Step.objects.get(number=2, name='step_second', description='desc')
        step1 = Step.objects.get(number=1, name='step_first')
        self.assertEqual(str(step2),'2) step_second')
        self.assertEqual(str(step1), '1) step_first')

    def test_ordering(self):
        steps = Step.objects.all()
        self.assertEqual(steps[0].number,1)
        self.assertEqual(steps[1].number, 2)

