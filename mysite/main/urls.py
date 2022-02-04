from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [

    path('', views.prijava, name='prijava'),
    path('homepage_neregistrirani/', views.homepage_neregistrirani, name='homepage_neregistrirani'),
    path('vozila/', views.vozila, name='vozila'),
    path('proizvodaci/', views.proizvodaci, name='proizvodaci')
]
