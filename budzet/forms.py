
from django import forms
from .models import Transakcja, Kategoria

class TransakcjaForm(forms.ModelForm):
    class Meta:
        model = Transakcja
        fields = ['kwota', 'kategoria', 'opis', 'uzytkownik']
        exclude = ['data', 'uzytkownik']
