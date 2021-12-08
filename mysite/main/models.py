from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Proizvodac( models.Model ):
    sifra_proizvodaca = models.CharField( max_length=10 )
    naziv_proizvodaca = models.CharField( max_length= 50 )

    def __str__( self ):
        return self.sifra_proizvodaca

class Vozilo( models.Model ):
    sifra_vozila = models.CharField( max_length= 10 )
    vrsta_vozila = models.CharField( max_length= 30 )
    naziv_proizvodaca = models.ForeignKey( Proizvodac, on_delete= models.CASCADE )
    model_vozila = models.CharField( max_length= 30 )
    godina_proizvodnje = models.CharField( max_length= 10 )
    kilometraza = models.CharField( max_length= 25 )
    boja = models.CharField( max_length= 20 )
    cijena = models.CharField( max_length= 25 )

    def __str__( self ):
        return self.sifra_vozila

class Korisnik( models.Model ):
    username = models.CharField( max_length= 50 )
    password = models.CharField( max_length=  50)
    uloga = models.CharField( max_length= 30 )

    def __str__( self ):
        return self.username

class Message( models.Model ):
    posiljatelj = models.ForeignKey( Korisnik, related_name= "posiljatelj", on_delete=models.CASCADE )
    primatelj = models.ForeignKey( Korisnik, related_name= "primatelj", on_delete=models.CASCADE )
    text = models.CharField( max_length= 4096 )
    vrijeme = models.DateTimeField( )
    procitano = models.BooleanField( default= False )

    def __str__( self ):
        return "{} to {}: {}".format(self.posiljatelj, self.primatelj, self.text)
