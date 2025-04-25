from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Transakcja(models.Model):
    data = models.DateTimeField()
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.CharField(max_length=255)
    kategoria = models.ForeignKey('Kategoria', on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    typ = models.CharField(max_length=50)

class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, null=True, blank=True)
