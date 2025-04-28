from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TransakcjaForm
from .models import Transakcja, Kategoria 
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'budzet/home.html')

def dodaj_transakcje(request):
    if request.method == 'POST':
        form = TransakcjaForm(request.POST)
        if form.is_valid():
            transakcja = form.save(commit=False)  # NIE zapisujemy jeszcze do bazy!
            transakcja.uzytkownik = request.user  # Automatycznie przypisujemy aktualnie zalogowanego użytkownika
            transakcja.save()  # Teraz zapisujemy!
            return redirect('lista_transakcji')  # lub gdziekolwiek chcesz
    else:
        form = TransakcjaForm()
    return render(request, 'budzet/dodaj_transakcje.html', {'form': form})

def lista_transakcji(request):
    transakcje = Transakcja.objects.all()  # Pobieramy wszystkie transakcje
    return render(request, 'budzet/lista_transakcji.html', {'transakcje': transakcje})

@login_required(login_url='/login/')
def dodaj_transakcje(request):
    ...