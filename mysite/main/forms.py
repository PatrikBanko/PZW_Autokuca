from attr import fields
from django import forms
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


#ZA PORUKE
class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)