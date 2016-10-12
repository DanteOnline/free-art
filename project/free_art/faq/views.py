from faq.models import Faq
from django.views.generic.list import ListView
# Create your views here.
class FaqListView(ListView):
    model = Faq
    template_name = 'faq.html'
    paginate_by = 100
