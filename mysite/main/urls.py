from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('vozila/', views.vozila, name='vozila'),
    path('proizvodaci/', views.proizvodaci, name='proizvodaci')
]
