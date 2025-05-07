# Wybieramy obraz z Pythonem
FROM python:3.13.3

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki
COPY . .

# Instalujemy zależności
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Otwieramy port 8000
EXPOSE 8000

# Komenda uruchomienia serwera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]