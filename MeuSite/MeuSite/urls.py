"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from MeuApp import views as meuAppViews
from MeuSite import views as meuSiteViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', meuAppViews.home, name='homepage'),
    path('SegundaPagina', meuAppViews.segundaPagina, name='segunda'),
    path("contatos/", include ('contatos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('seguranca/', meuSiteViews.homeSec, name='sec-home'),
]