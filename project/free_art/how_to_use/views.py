from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HowToUseView(TemplateView):
    template_name = 'how_to_use.html'