from multiprocessing import context
from typing import Container
from urllib import request
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.views.generic import ListView
from .forms import *
from django.contrib.auth.models import *
from .filters import VoziloFilter
from django.views import View
from django.db.models import Q


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

    if request.method == "POST":
        vozilo.delete()
        return redirect("/vozila_registrirani")

    context = {"vozilo": vozilo}
    return render(request, "./delete_vozilo.html", context)


def updateProizvodac(request, pk):
    proizvodac = Proizvodac.objects.get(sifra_proizvodaca=pk)
    form = ProizvodacForm(instance=proizvodac)

    if request.method == "POST":
        form = ProizvodacForm(request.POST, instance=proizvodac)
        if form.is_valid():
            form.save()
            return redirect("/proizvodaci_registrirani")

    context = {"form": form}
    return render(request, "./novi_unos_proizvodac.html", context=context)


def deleteProizvodac(request, pk):
    proizvodac = Proizvodac.objects.get(sifra_proizvodaca=pk)

    if request.method == "POST":
        proizvodac.delete()
        return redirect("/proizvodaci_registrirani")

    context = {"proizvodac": proizvodac}
    return render(request, "./delete_proizvodac.html", context)


def filter(request):
    vozilo_list = Vozilo.objects.all()
    vozilo_filter = VoziloFilter(request.GET, queryset=vozilo_list)
    return render(request, "vozilo_list.html", {"filter": vozilo_filter})


def filter_ne_registrirani(request):
    vozilo_list = Vozilo.objects.all()
    vozilo_filter = VoziloFilter(request.GET, queryset=vozilo_list)
    return render(request, "vozilo_list_neregistrirani.html", {"filter": vozilo_filter})


# ZA PORUKE
class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {"threads": threads}

        return render(request, "social/inbox.html", context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {"form": form}

        return render(request, "social/create_thread.html", context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get("username")

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect("thread", pk=thread.pk)
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect("thread", pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(user=request.user, receiver=receiver)
                thread.save()

                return redirect("thread", pk=thread.pk)
        except:
            return redirect("create-thread")


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)

        context = {"thread": thread, "form": form, "message_list": message_list}

        return render(request, "social/thread.html", context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread, sender_user=request.user, receiver_user=receiver, body=request.POST.get("message")
        )

        message.save()
        return redirect("thread", pk=pk)
