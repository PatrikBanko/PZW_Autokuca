from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):
    def test_homepage_neregistrirani(self):
        url = reverse("homepage_neregistrirani")

        self.assertEquals(resolve(url).func, homepage_neregistrirani)

    def test_vozila_neregistrirani(self):
        url = reverse("vozila_neregistrirani")

        self.assertEquals(resolve(url).func, vozila_neregistrirani)

    def test_proizvodaci_neregistrirani(self):
        url = reverse("proizvodaci_neregistrirani")

        self.assertEquals(resolve(url).func, proizvodaci_neregistrirani)

    def test_homepage_registrirani(self):
        url = reverse("homepage_registrirani")

        self.assertEquals(resolve(url).func, homepage_registrirani)

    def test_vozila_registrirani(self):
        url = reverse("vozila_registrirani")

        self.assertEquals(resolve(url).func, vozila_registrirani)

    def test_proizvodaci_registrirani(self):
        url = reverse("proizvodaci_registrirani")

        self.assertEquals(resolve(url).func, proizvodaci_registrirani)

    def test_update_vozilo(self):
        url = reverse("update_vozilo", args=["some-vozilo"])

        self.assertEquals(resolve(url).func, updateVozilo)
