from django import forms
from .models import Transakcja
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class TransakcjaForm(forms.ModelForm):
    class Meta:
        model = Transakcja
        fields = ['kwota', 'kategoria', 'opis']
        exclude = ['data', 'uzytkownik']

class RejestracjaForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ten adres email jest już zarejestrowany.")
        return email
