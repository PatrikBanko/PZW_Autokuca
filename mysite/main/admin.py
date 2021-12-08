from django.contrib import admin
from .models import *

# Register your models here.
model_list = [ Vozilo, Proizvodac, Korisnik, Message ]
admin.site.register( model_list )