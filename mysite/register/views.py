from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registracija(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            print("Uspjesno")
        #TODO dodati redirect     
        return redirect("/")
    else:
        form = UserCreationForm()

    return render(response, "register/registracija.html", {"form":form})

def prijava(request):
    return render(request, "./registration/login.html")