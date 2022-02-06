# PZW_Autokuca

Aplikacija Autokuća omogućuje pregled stanja trima vrstama korisnika: neregistriranim korisnicima, registriranim korisnicima te adminu. Pri tome, neregistrirani korisnici mogu samo pregledavati stanje autokuće te filtrirati (pretraživati), registrirani korisnici se prijavljuju nakon čega imaju mogućnost pregledavanja, filtriranja, slanja međusobnih poruka i dodavanja automobila za prodaju, dok admin može pregledavati, filtrirati, unositi, izmjenjivati i brisati sva vozila. Prema ovom opisu datoteka models.py je konstruirana na način da imamo 4 klase: Proizvodac, Vozilo, Korisnik i Message. U klasi Proizvodac nalaze se šifra te naziv proizvođača tipa CharField. Klasa Vozilo sadrži šifru vozila, vrstu vozila (osobno vozilo, motocikl,...), naziv proizvođača, model vozila, godinu proizvodnje, kilometražu, boju, cijenu i kontakt. Pri tome, šifra vozila, vrsta vozila, model vozila, godina proizvodnje, kilometraža, boja i cijena su tipa CharField, a naziv proizvođača i kontakt su vanjski ključevi klasa Proizvođač i Korisnik. U klasi Korisnik su atributi username, password i uloga tipa CharField. Posljednja klasa Message sadrži pošiljatelja, primatelja, tekst, vrijeme i boolean atribut pročitano. Primatelj i pošiljatelj su vanjski ključevi klase Korisnik, vrijeme je tipa DateTimeField, a tekst je tipa CharField.


Potrebno je:
pip install django-crispy-forms
pip install attr
pip3 install cattrs==1.0.0