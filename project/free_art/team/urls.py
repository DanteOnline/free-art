from django.conf.urls import url
from team.views import TeamTemplateView

urlpatterns = [
    url(r'^$',TeamTemplateView.as_view(),name='team')
]