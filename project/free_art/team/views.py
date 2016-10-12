from django.shortcuts import render
from team.models import Tester, Developer
from django.views.generic.base import TemplateView

# Create your views here.
class TeamTemplateView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        developers = Developer.objects.all()
        context['developers'] = developers
        testers = Tester.objects.all()
        context['testers'] = testers
        return context