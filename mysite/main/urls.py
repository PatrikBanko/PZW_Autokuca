from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from register import views as v

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [

    path('', v.registracija, name="registracija"),
    path('homepage_neregistrirani/', views.homepage_neregistrirani, name='homepage_neregistrirani'),
    path('vozila/', views.vozila, name='vozila'),
    path('proizvodaci/', views.proizvodaci, name='proizvodaci'),
    
]
