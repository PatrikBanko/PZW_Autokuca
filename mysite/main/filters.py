from django.contrib.auth.models import *
import django_filters
from .models import *

class VoziloFilter(django_filters.FilterSet):
    class Meta:
        model = Vozilo
        fields = ['model_vozila', 'naziv_proizvodaca','vrsta_vozila', 'cijena', 'godina_proizvodnje' ]