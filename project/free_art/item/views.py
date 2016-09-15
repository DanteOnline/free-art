from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from item.models import Script
from django.views.generic.base import ContextMixin
from item.models import Category
from django.core.urlresolvers import reverse

class CategoryMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(CategoryMixin, self).get_context_data(**kwargs)
        context['top_list'] = Category.get_top_list()
        return context

class CategoryDetailView(DetailView, CategoryMixin):
    model = Category
    template_name = 'category.html'

class ScriptDetailView(DetailView, CategoryMixin):
    model = Script
    template_name = 'item.html'

