from multiprocessing import context
from typing import Container
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.views.generic import ListView

## Create your views here.

def prijava(request):
    return render(request, "./homepage_neregistrirani.html")

def homepage_neregistrirani(request):
    return render(request, "./homepage_neregistrirani.html")

def vozila_neregistrirani(request):
    try: 
        vozila=Vozilo.objects.all()
        context={"vozila":vozila}
    except Vozilo.DoesNotExist:
        raise Http404("Vozilo ne postoji!")
    return render(request, "./vozila_neregistrirani.html", context=context)

def proizvodaci_neregistrirani(request):
    try: 
        proizvodaci=Proizvodac.objects.all()
        context={"proizvodaci":proizvodaci}
    except Proizvodac.DoesNotExist:
        raise Http404("Proizvodac ne postoji!")
    return render(request, "./proizvodaci_neregistrirani.html", context=context)

    