"""free_art URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^items/', include('item.urls')),
    url(r'^', include('main.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'comments/', include('django_comments.urls')),
    url(r'team/', include('team.urls')),
    url(r'about/', include('about.urls')),
    url(r'contact', include('contact.urls')),
    url(r'how_to_use', include('how_to_use.urls')),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
