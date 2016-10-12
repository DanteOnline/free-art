from django.shortcuts import render
from django.views.generic.list import ListView
from how_to_use.models import Subject

class How2UseListView(ListView):
    model = Subject

