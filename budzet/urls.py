from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dodaj/', views.dodaj_transakcje, name='dodaj_transakcje'),
    path('lista/', views.lista_transakcji, name='lista_transakcji'), 
    path('login/', auth_views.LoginView.as_view(template_name='budzet/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
]