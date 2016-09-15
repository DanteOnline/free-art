from django.conf.urls import url
from item.views import CategoryDetailView, ScriptDetailView

urlpatterns = [
    url(r'^category/(?P<pk>\d+)?$', CategoryDetailView.as_view(), name='category'),
    url(r'^script/(?P<pk>\d+)?$', ScriptDetailView.as_view(), name='script'),
]