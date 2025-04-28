from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    NAZWY_KATEGORII = [
        ('żywność', 'Żywność'),
        ('transport', 'Transport'),
        ('mieszkanie', 'Mieszkanie'),
        ('rozrywka', 'Rozrywka'),
        ('inne', 'Inne'),
    ]

    nazwa = models.CharField(max_length=100, choices=NAZWY_KATEGORII)
    opis = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return self.nazwa


class Transakcja(models.Model):
    NAZWY_KATEGORII = [
        ('żywność', 'Żywność'),
        ('transport', 'Transport'),
        ('mieszkanie', 'Mieszkanie'),
        ('rozrywka', 'Rozrywka'),
        ('inne', 'Inne'),
    ]
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.CharField(max_length=50, choices=NAZWY_KATEGORII)
    data = models.DateTimeField(auto_now_add=True)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    opis = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tytul} - {self.kwota}"


class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, null=True, blank=True)  
    adres = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return self.user.username
