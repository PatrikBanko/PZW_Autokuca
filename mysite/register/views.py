from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import *


# Create your views here.
def registracija(response):
    if response.user.is_authenticated:
        logout(response)

    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            print("Uspjesno")
        return redirect("/")
    else:
        form = UserCreationForm()

    return render(response, "register/registracija.html", {"form": form})


def prijava(request):
    return render(request, "./registration/login.html")
