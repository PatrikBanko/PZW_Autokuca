from django.test import TestCase
from main.models import *


class TestProizvodac(TestCase):
    def setUp(self):
        self.proizvodac1 = Proizvodac.objects.create(
            sifra_proizvodaca="some-proizvodac", naziv_proizvodaca="TestProizvodac"
        )

    def test_proizvodac(self):
        self.assertEquals(self.proizvodac1.naziv_proizvodaca, "TestProizvodac")


class TestVozilo(TestCase):
    def setUp(self):
        naziv_p = Proizvodac.objects.create(
            sifra_proizvodaca="some-proizvodac", naziv_proizvodaca="Test"
        )
        
        self.vozilo1 = Vozilo.objects.create(
            sifra_vozila="1",
            vrsta_vozila="automobil",
            model_vozila="Audi",
            godina_proizvodnje="2015",
            kilometraza="60000",
            boja="TestBoja",
            cijena="20000",
            naziv_proizvodaca=naziv_p,
        )

    def test_vozilo(self):
        self.assertEquals(self.vozilo1.model_vozila, "Audi")
