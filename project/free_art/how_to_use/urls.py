from django.conf.urls import url
from how_to_use.views import HowToUseView

urlpatterns = [
    url(r'^$',HowToUseView.as_view(),name = 'how_to_use')
]