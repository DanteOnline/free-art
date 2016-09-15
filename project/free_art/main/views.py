from django.shortcuts import render
from django.views.generic.base import TemplateView
from item.views import CategoryMixin

# Create your views here.
class MainView(TemplateView, CategoryMixin):
    template_name = 'index.html'
