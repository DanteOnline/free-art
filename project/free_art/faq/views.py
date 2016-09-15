from faq.models import Faq
from django.views.generic.list import ListView
from item.views import CategoryMixin
# Create your views here.
class FaqListView(ListView, CategoryMixin):
    model = Faq
    template_name = 'faq.html'
    paginate_by = 100
