from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from register import views as v
from django.urls import re_path

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [

    path('', v.registracija, name="registracija"),
    path('homepage_neregistrirani/', views.homepage_neregistrirani, name='homepage_neregistrirani'),
    path('vozila_neregistrirani/', views.vozila_neregistrirani, name='vozila_neregistrirani'),
    path('proizvodaci_neregistrirani/', views.proizvodaci_neregistrirani, name='proizvodaci_neregistrirani'),

    path('homepage_registrirani/', views.homepage_registrirani, name='homepage_registrirani'),
    path('proizvodaci_registrirani/', views.proizvodaci_registrirani, name='proizvodaci_registrirani'),
    path('novi_unos_vozilo/', views.noviUnosVozilo, name="novi_unos_vozilo"),
    path('novi_unos_proizvodac/', views.noviUnosProizvodac, name="novi_unos_proizvodaci"),
    re_path(r'^filter/$', views.filter, name='filter'), 
    re_path(r'^filter_ne_registrirani/$', views.filter_ne_registrirani, name='filter_ne_registrirani'), 

]

