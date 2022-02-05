from multiprocessing import context
from typing import Container
from urllib import request
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.views.generic import ListView
from .forms import *

## Create your views here.


def prijava(request):
    return render(request, "./homepage_neregistrirani.html")


def homepage_neregistrirani(request):
    return render(request, "./homepage_neregistrirani.html")


def homepage_registrirani(request):
    return render(request, "./homepage_registrirani.html")


def vozila_neregistrirani(request):
    try:
        vozila = Vozilo.objects.all()
        context = {"vozila": vozila}
    except Vozilo.DoesNotExist:
        raise Http404("Vozilo ne postoji!")
    return render(request, "./vozila_neregistrirani.html", context=context)


def vozila_registrirani(request):
    try:
        vozila = Vozilo.objects.all()
        context = {"vozila": vozila}
    except Vozilo.DoesNotExist:
        raise Http404("Vozilo ne postoji!")
    return render(request, "./vozila_registrirani.html", context=context)


def proizvodaci_neregistrirani(request):
    try:
        proizvodaci = Proizvodac.objects.all()
        context = {"proizvodaci": proizvodaci}
    except Proizvodac.DoesNotExist:
        raise Http404("Proizvodac ne postoji!")
    return render(request, "./proizvodaci_neregistrirani.html", context=context)


def proizvodaci_registrirani(request):
    try:
        proizvodaci = Proizvodac.objects.all()
        context = {"proizvodaci": proizvodaci}
    except Proizvodac.DoesNotExist:
        raise Http404("Proizvodac ne postoji!")
    return render(request, "./proizvodaci_registrirani.html", context=context)


def noviUnosVozilo(request):

    form = VoziloForm()
    if request.method == "POST":
        # print('Printing POST: ', request.POST)
        form = VoziloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vozila_registrirani")

    context = {"form": form}
    return render(request, "./novi_unos_vozilo.html", context=context)


def noviUnosProizvodac(request):
    form = ProizvodacForm()
    if request.method == "POST":
        form = ProizvodacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/proizvodaci_registrirani")

    context = {"form": form}
    return render(request, "./novi_unos_proizvodac.html", context=context)


def updateVozilo(request, pk):
    vozilo = Vozilo.objects.get(sifra_vozila=pk)
    form = VoziloForm(instance=vozilo)

    if request.method == "POST":
        form = VoziloForm(request.POST, instance=vozilo)
        if form.is_valid():
            form.save()
            return redirect("/vozila_registrirani")

    context = {"form": form}
    return render(request, "./novi_unos_vozilo.html", context=context)


def deleteVozilo(request, pk):
    vozilo = Vozilo.objects.get(sifra_vozila=pk)

    if request.method=='POST':
        vozilo.delete()
        return redirect('/vozila_registrirani')

    context = {"vozilo": vozilo}
    return render(request, "./delete_vozilo.html", context)
