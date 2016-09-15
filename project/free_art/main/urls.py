from main.views import MainView
from django.conf.urls import url

urlpatterns = [
    url(r'^$',MainView.as_view(),name='index')
]