from attr import fields
from django.forms import ModelForm
from .models import *


class VoziloForm(ModelForm):
    class Meta:
        model = Vozilo
        fields = '__all__'

class ProizvodacForm(ModelForm):
    class Meta:
        model = Proizvodac
        fields = '__all__'