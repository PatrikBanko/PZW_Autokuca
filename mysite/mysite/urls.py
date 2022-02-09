"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from register import views as v
from main import views as vm
from main.views import *

from django.urls import re_path

urlpatterns = [
    path('', include('main.urls')), #dodajemo urls
    path('admin/', admin.site.urls),
    path('registracija/', v.registracija, name="registracija"),
    path('', include("django.contrib.auth.urls")),
    path('update_vozilo/<str:pk>/', vm.updateVozilo, name="update_vozilo"),
    path('delete_vozilo/<str:pk>/', vm.deleteVozilo, name="delete_vozilo"),
    path('vozila_registrirani/', vm.vozila_registrirani, name='vozila_registrirani'),
    path('update_proizvodac/<str:pk>/', vm.updateProizvodac, name="update_proizvodac"),
    path('delete_proizvodac/<str:pk>/', vm.deleteProizvodac, name="delete_proizvodac"),
    path('proizvodaci_registrirani/', vm.proizvodaci_registrirani, name='proizvodaci_registrirani'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),




    path('', v.registracija, name="registracija"),
    path('homepage_neregistrirani/', vm.homepage_neregistrirani, name='homepage_neregistrirani'),
    path('vozila_neregistrirani/', vm.vozila_neregistrirani, name='vozila_neregistrirani'),
    path('proizvodaci_neregistrirani/', vm.proizvodaci_neregistrirani, name='proizvodaci_neregistrirani'),

    path('homepage_registrirani/', vm.homepage_registrirani, name='homepage_registrirani'),
    path('proizvodaci_registrirani/', vm.proizvodaci_registrirani, name='proizvodaci_registrirani'),
    path('novi_unos_vozilo/', vm.noviUnosVozilo, name="novi_unos_vozilo"),
    path('novi_unos_proizvodac/', vm.noviUnosProizvodac, name="novi_unos_proizvodaci"),
    re_path(r'^filter/$', vm.filter, name='filter'), 
    re_path(r'^filter_ne_registrirani/$', vm.filter_ne_registrirani, name='filter_ne_registrirani'), 
]
