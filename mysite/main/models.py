from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Proizvodac(models.Model):
    sifra_proizvodaca = models.CharField(max_length=10)
    naziv_proizvodaca = models.CharField(max_length=50)

    def __str__(self):
        return self.naziv_proizvodaca


class Vozilo(models.Model):
    sifra_vozila = models.CharField(max_length=10)
    vrsta_vozila = models.CharField(max_length=30)
    naziv_proizvodaca = models.ForeignKey(Proizvodac, on_delete=models.CASCADE)
    model_vozila = models.CharField(max_length=30)
    godina_proizvodnje = models.IntegerField()
    kilometraza = models.IntegerField()
    boja = models.CharField(max_length=20)
    cijena = models.IntegerField()

    def __str__(self):
        return self.model_vozila


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name="user", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class Message( models.Model ):
#     posiljatelj = models.ForeignKey( Korisnik, related_name= "posiljatelj", on_delete=models.CASCADE )
#     primatelj = models.ForeignKey( Korisnik, related_name= "primatelj", on_delete=models.CASCADE )
#     text = models.CharField( max_length= 4096 )
#     vrijeme = models.DateTimeField( )
#     procitano = models.BooleanField( default= False )

#     def __str__( self ):
#         return "{} to {}: {}".format(self.posiljatelj, self.primatelj, self.text)


class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    has_unread = models.BooleanField(default=False)


class MessageModel(models.Model):
    thread = models.ForeignKey("ThreadModel", related_name="+", on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
