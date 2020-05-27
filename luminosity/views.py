from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def luminosity(request):
    # Verifica si hay un parámetro Tipo en la petición GET
    if 'Valor' in request.GET:
        Valor = request.GET['Valor']
        Tipo = request.GET['Tipo']
        latitud = request.GET['latitud']
        longitud = request.GET['longitud']
        # Verifica si el Tipo no esta vacio
        if Tipo:
            # Crea el json para realizar la petición POST al Web Service
            args = {'Tipo': Tipo , 'Valor': Valor, 'latitud': latitud, 'longitud': longitud}
            response = requests.post('http://127.0.0.1:8000/luminositys/', args)
            response = requests.post('https://pi1-eafit-sarboledab.azurewebsites.net/luminositys/', args)
            # Convierte la respuesta en JSON
            luminosity_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/luminositys/')
    # Convierte la respuesta en JSON
    luminositys = response.json()
    # Rederiza la respuesta en el template luminosity
    return render(request, "luminosity/luminosity.html", {'luminositys': luminositys})