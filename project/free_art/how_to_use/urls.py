from how_to_use.views import How2UseListView
from django.conf.urls import url

urlpatterns = [
    url('^$',How2UseListView.as_view(),name='how2use')
]